from db import DB


class CoffeeMachine:
    COIN_VALUES = {"penny": 1, "nickel": 5, "dime": 10, "quarter": 25}
    COIN_ALIASES = {
        "penny": "penny", "pennies": "penny",
        "nickel": "nickel", "nickels": "nickel",
        "dime": "dime", "dimes": "dime",
        "quarter": "quarter", "quarters": "quarter",
        "qarter": "quarter",  # Compatibility with the seed-data typo.
    }

    def __init__(self):
        self.db = DB()

    def get_drinks(self):
        self.db.execute("SELECT * FROM drinks")
        return self.db.fetchall()

    def buy_drink(self, drink_id, coins_inserted):
        """Buy a drink with input such as {"quarters": 4, "dimes": 2}."""
        try:
            inserted = self._normalise_coins(coins_inserted)
        except (TypeError, ValueError) as error:
            return str(error)

        self.db.execute("SELECT * FROM drinks WHERE id = ?", (drink_id,))
        drink = self.db.fetchone()
        if drink is None:
            return "Drink not found. Coins returned."

        price = int(round(drink[7]))
        inserted_total = self._coin_total(inserted)

        if inserted_total < price:
            self._record_transaction(drink_id, inserted, 0, "FAILED")
            return (
                f"Not enough coins inserted. {self._format_money(inserted_total)} inserted; "
                f"{self._format_money(price)} required. Coins returned."
            )

        needed_ingredients = {
            "milk": drink[2],
            "coffee": drink[4],
            "cocoa": drink[5],  # The Drinks table spells this column "cacoa".
            "vanilla": drink[6],
        }
        self.db.execute("SELECT name, quantity FROM ingredients")
        inventory = {name.lower(): quantity for name, quantity in self.db.fetchall()}
        missing = [
            name for name, needed in needed_ingredients.items()
            if needed > inventory.get(name, 0)
        ]
        if missing:
            self._record_transaction(drink_id, inserted, 0, "FAILED")
            return "Not enough ingredients: " + ", ".join(missing) + ". Coins returned."

        self.db.execute("SELECT id, name, value, count FROM coins")
        available, coin_ids, values = {}, {}, {}
        for coin_id, name, value, count in self.db.fetchall():
            coin_type = self.COIN_ALIASES.get(name.lower())
            if coin_type:
                coin_ids[coin_type] = coin_id
                values[coin_type] = int(round(value))
                # Inserted coins may be used while making the customer's change.
                available[coin_type] = int(count) + inserted[coin_type]

        change_due = inserted_total - price
        returned = self._find_exact_change(change_due, available, values)
        if returned is None:
            self._record_transaction(drink_id, inserted, 0, "FAILED")
            return f"Unable to return exact change of {self._format_money(change_due)}. Coins returned."

        # Coin stock, ingredients, and the transaction are one atomic sale.
        try:
            for coin_type, count in available.items():
                self.db.execute(
                    "UPDATE coins SET count = ? WHERE id = ?",
                    (count - returned.get(coin_type, 0), coin_ids[coin_type]),
                    commit=False,
                )
            for name, needed in needed_ingredients.items():
                if needed:
                    self.db.execute(
                        "UPDATE ingredients SET quantity = quantity - ? WHERE lower(name) = ?",
                        (needed, name),
                        commit=False,
                    )
            self._record_transaction(
                drink_id, inserted, change_due, "SUCCESS", commit=False
            )
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

        return (
            f"Drink {drink[1]} purchased successfully. Change returned: "
            f"{self._format_money(change_due)} ({self._format_coins(returned)})."
        )

    def coin_change(self, coins_inserted, drink_price):
        """Check exact change without altering the machine's inventory."""
        try:
            inserted = self._normalise_coins(coins_inserted)
        except (TypeError, ValueError) as error:
            return str(error)

        change_due = self._coin_total(inserted) - int(round(drink_price))
        if change_due < 0:
            return "Not enough coins inserted. Coins returned."

        self.db.execute("SELECT name, value, count FROM coins")
        available, values = {}, {}
        for name, value, count in self.db.fetchall():
            coin_type = self.COIN_ALIASES.get(name.lower())
            if coin_type:
                values[coin_type] = int(round(value))
                available[coin_type] = int(count) + inserted[coin_type]

        returned = self._find_exact_change(change_due, available, values)
        if returned is None:
            return f"Unable to return exact change of {self._format_money(change_due)}. Coins returned."
        return f"Change returned: {self._format_money(change_due)} ({self._format_coins(returned)})."

    def _normalise_coins(self, coins_inserted):
        if not isinstance(coins_inserted, dict):
            raise TypeError("coins_inserted must be a dictionary of coin type and count.")
        coins = {coin_type: 0 for coin_type in self.COIN_VALUES}
        for supplied_type, count in coins_inserted.items():
            coin_type = self.COIN_ALIASES.get(str(supplied_type).strip().lower())
            if coin_type is None:
                raise ValueError(f"Unknown coin type: {supplied_type}.")
            if isinstance(count, bool) or not isinstance(count, int):
                raise ValueError(f"Coin count for {supplied_type} must be an integer.")
            if count < 0:
                raise ValueError(f"Coin count for {supplied_type} cannot be negative.")
            coins[coin_type] += count
        return coins

    def _coin_total(self, coins):
        return sum(self.COIN_VALUES[name] * count for name, count in coins.items())

    @staticmethod
    def _format_money(cents):
        return f"${cents / 100:.2f}"

    @staticmethod
    def _find_exact_change(amount, available, values):
        """Find exact change with limited coin stock; return None if impossible."""
        solutions = {0: {coin_type: 0 for coin_type in available}}
        for coin_type in sorted(available, key=lambda item: values[item], reverse=True):
            value = values[coin_type]
            for subtotal, solution in list(solutions.items()):
                maximum = min(available[coin_type], (amount - subtotal) // value)
                for count in range(1, maximum + 1):
                    total = subtotal + count * value
                    candidate = solution.copy()
                    candidate[coin_type] = count
                    current = solutions.get(total)
                    if current is None or sum(candidate.values()) < sum(current.values()):
                        solutions[total] = candidate
        return solutions.get(amount)

    def _record_transaction(
        self, drink_id, inserted, change, status, commit=True
    ):
        self.db.execute(
            """
            INSERT INTO transactions (
                drink_id, inserted_pennies, inserted_nickels,
                inserted_dimes, inserted_quarters, change_returned, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (drink_id, inserted["penny"], inserted["nickel"], inserted["dime"],
             inserted["quarter"], change, status),
            commit=commit,
        )

    @staticmethod
    def _format_coins(coins):
        plurals = {"penny": "pennies"}
        used = [
            f"{count} {name if count == 1 else plurals.get(name, name + 's')}"
            for name, count in coins.items() if count
        ]
        return ", ".join(used) if used else "no coins"


def _read_non_negative_integer(message):
    """Keep asking until the user supplies a whole number of zero or more."""
    while True:
        try:
            value = int(input(message))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a whole number that is zero or greater.")


def main():
    """Run the coffee machine from the terminal to test the purchase flow."""
    machine = CoffeeMachine()

    try:
        while True:
            print("\nAvailable drinks")
            print("----------------")
            for drink in machine.get_drinks():
                price = machine._format_money(int(round(drink[7])))
                print(f"{int(drink[0]):>2}. {drink[1]:<24} {price}")

            selection = input("\nEnter a drink ID, or Q to quit: ").strip()
            if selection.lower() == "q":
                print("Goodbye!")
                break

            try:
                drink_id = int(selection)
            except ValueError:
                print("Please enter a valid drink ID.")
                continue

            print("\nInsert coins by entering the count of each coin type.")
            coins_inserted = {
                "pennies": _read_non_negative_integer("Pennies  (1 cent):  "),
                "nickels": _read_non_negative_integer("Nickels   (5 cents): "),
                "dimes": _read_non_negative_integer("Dimes    (10 cents): "),
                "quarters": _read_non_negative_integer("Quarters (25 cents): "),
            }

            total = machine._coin_total(machine._normalise_coins(coins_inserted))
            print(f"\nTotal inserted: {machine._format_money(total)}")
            print(machine.buy_drink(drink_id, coins_inserted))

            again = input("\nWould you like another drink? (y/n): ").strip().lower()
            if again not in ("y", "yes"):
                print("Goodbye!")
                break
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
    finally:
        machine.db.close()


if __name__ == "__main__":
    main()
