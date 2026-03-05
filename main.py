# main.py

import calculator

def main():
    calc = calculator.Calculator()
    print("Quick-Calc CLI")
    print("Enter numbers and operations (+, -, *, /), = to calculate, C to clear, Q to quit")
    while True:
        user_input = input("Input: ")
        if user_input.isdigit():
            calc.input_number(int(user_input))
        elif user_input in ['+', '-', '*', '/']:
            calc.input_operation(user_input)
        elif user_input == '=':
            calc.calculate()
        elif user_input == 'C':
            calc.clear()
        elif user_input == 'Q':
            break
        else:
            print("Invalid input")
        print("Display:", calc.get_display())

if __name__ == "__main__":
    main()