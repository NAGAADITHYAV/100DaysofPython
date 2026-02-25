from art import LOGO, WIN, LOSE, DRAW
from blackjack import BlackJack


class Table:
    def __init__(self):
        self.blackjack = BlackJack()
        self.chips = self._prompt_positive_int("How many chips do you want to start with? ")

    def reset_deck(self):
        self.blackjack = BlackJack()

    def play(self):
        while self.chips > 0:
            hand, bet = self._start_round()
            round_state, bet = self._play_player_turn(hand, bet)
            self._finalize_round(hand, bet, round_state)

            self._print_chips()
            if self._cash_out():
                print(f"You have cashed out with {self.chips} chips.")
                break
            if self._reset():
                self.reset_deck()

    def _start_round(self):
        bet = self._take_initial_bet()
        hand = self.blackjack.deal_hand()
        return hand, bet

    def _take_initial_bet(self):
        while True:
            bet = self._prompt_positive_int("How many chips do you want to bet? ")
            if bet > self.chips:
                print("You do not have enough chips to make this bet.")
                continue
            self.chips -= bet
            return bet

    def _play_player_turn(self, hand, bet):
        player_has_hit = False

        while True:
            self.blackjack.display_in_game(hand)
            if self.blackjack.is_bust(hand["player_hand"]):
                return "bust", bet
            if self.blackjack.is_blackjack(hand["player_hand"]):
                return "blackjack", bet

            can_bet_more = self._can_bet_more(player_has_hit, hand)
            can_split = can_bet_more and self.blackjack.can_split(hand["player_hand"])
            action = self._prompt_player_action(can_bet_more, can_split)

            if action == "h":
                self.blackjack.hit(hand["player_hand"])
                player_has_hit = True
                continue

            if action == "s":
                return "stand", bet

            if action == "b" and can_bet_more:
                bet = self._bet_more(bet)
                continue

            if action == "p" and can_split:
                print("Split is not implemented yet, but the design supports adding it.")
                continue

            print("Invalid option. Try again.")

    def _can_bet_more(self, player_has_hit, hand):
        return not player_has_hit and len(hand["player_hand"]) == 2 and self.chips > 0

    def _prompt_player_action(self, can_bet_more, can_split):
        options = ["HIT(h)", "STAND(s)"]
        if can_bet_more:
            options.append("BET MORE(b)")
        if can_split:
            options.append("SPLIT(p)")
        return input(f"Enter {' / '.join(options)}: ").strip().lower()

    def _bet_more(self, current_bet):
        while True:
            additional_bet = self._prompt_positive_int(f"How many additional chips? (max {self.chips}): ")
            if additional_bet > self.chips:
                print("You do not have enough chips for that additional bet.")
                continue
            self.chips -= additional_bet
            return current_bet + additional_bet

    def _finalize_round(self, hand, bet, round_state):
        if round_state == "bust":
            self._lose_round()
            return

        if round_state == "blackjack":
            self._win_round(bet)
            return

        self.blackjack.play_dealer_turn(hand["dealer_hand"])
        self.blackjack.display_final_game(hand)

        outcome = self.blackjack.resolve_round(hand["player_hand"], hand["dealer_hand"])
        if outcome == "win":
            self._win_round(bet)
        elif outcome == "lose":
            self._lose_round()
        else:
            self._draw_round(bet)

    def _win_round(self, bet):
        print(WIN)
        self.chips += 2 * bet

    def _lose_round(self):
        print(LOSE)

    def _draw_round(self, bet):
        print(DRAW)
        self.chips += bet

    def _prompt_positive_int(self, message):
        while True:
            try:
                value = int(input(message))
                if value <= 0:
                    print("Please enter a positive number.")
                    continue
                return value
            except ValueError:
                print("Please enter a valid number.")

    def _print_chips(self):
        print(f"You have {self.chips} chips remaining")

    def _cash_out(self):
        return input("Do you want to cash out? (y/n) ").strip().lower() == "y"

    def _reset(self):
        return input("Do you want to reset deck? (y/n) ").strip().lower() == "y"


if __name__ == "__main__":
    print("Welcome to the table of black jack!")
    print(LOGO)
    table = Table()
    table.play()
