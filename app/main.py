def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

class Calculator:
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
