# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

class Calculator:
    def __init__(self):
        self.display = "0"
        self.first_number = None
        self.operation = None
        self.waiting_for_second = False

    def input_number(self, num):
        if self.waiting_for_second:
            self.display = str(num)
            self.waiting_for_second = False
        else:
            if self.display == "0":
                self.display = str(num)
            else:
                self.display += str(num)

    def input_operation(self, op):
        if self.first_number is None:
            self.first_number = float(self.display)
        else:
            self.calculate()
        self.operation = op
        self.waiting_for_second = True

    def calculate(self):
        if self.operation and self.first_number is not None:
            second = float(self.display)
            if self.operation == '+':
                self.first_number = add(self.first_number, second)
            elif self.operation == '-':
                self.first_number = subtract(self.first_number, second)
            elif self.operation == '*':
                self.first_number = multiply(self.first_number, second)
            elif self.operation == '/':
                self.first_number = divide(self.first_number, second)
            self.display = str(self.first_number)
            self.operation = None

    def clear(self):
        self.display = "0"
        self.first_number = None
        self.operation = None
        self.waiting_for_second = False

    def get_display(self):
        return self.display