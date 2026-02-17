import art
from calculator import Calculator

def get_operation_result(n1, n2, op, calc_instance):
    """Handles the math logic based on the operator."""
    match op:
        case '+': return calc_instance.add(n1, n2)
        case '-': return calc_instance.subtract(n1, n2)
        case '*': return calc_instance.multiply(n1, n2)
        case '/': return calc_instance.divide(n1, n2)
        case '%': return calc_instance.remainder(n1, n2)
        case '^': return calc_instance.power(n1, n2)
        case _:   return 0

def start_calculator():
    print(art.LOGO)
    c = Calculator()
    res = None  # Use None to clearly signal "no previous result"

    while True:
        # 1. Get the first number (either from input or previous result)
        if res is None:
            n1 = int(input("Enter the first number: "))
        else:
            n1 = res
            print(f"Continuing with: {n1}")

        # 2. Get operation and second number
        op = input("Select operation (+, -, *, /, %, ^): ")
        n2 = int(input("Enter the next number: "))

        # 3. Calculate and display
        res = get_operation_result(n1, n2, op, c)
        print(f"Result: {res}")

        # 4. Determine next steps
        choice = input("\n[Enter] Continue | [S] Start Fresh | [E] End: ").upper()
        
        if choice == 'S':
            res = None
            print("\n" * 20) # Clear screen 'sim'
            print(art.LOGO)
        elif choice == 'E':
            print("Goodbye!")
            break

if __name__ == "__main__":
    start_calculator()