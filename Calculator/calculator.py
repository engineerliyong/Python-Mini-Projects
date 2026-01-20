"""
Calculator with History
Author: Liza Bambu
Date: January 2026

Interactive calculator that tracks calculation history.
"""
import datetime

def add(a, b):
    """Add two numbers"""
    added_value = a+b

    return added_value

def subtract(a, b):
    """Subtract b from a"""
    subtracted_value = a-b
    return subtracted_value

def multiply(a, b):
    """Multiply two numbers"""
    multiplied_value = a*b
    return multiplied_value

def divide(a, b):
    """Divide a by b"""
    
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_operation():
    valid_operations = ['+', '-', '*', '/', '**']
    while True:
        print("\nOperation: + (Add), - (Subtract), * (Multiply), / (Divide), ** (Power)")
        operation= input("Enter operation: ") .strip()

# Global list to store history


# Test them
if __name__ == "__main__":
    print(add(5, 3))        # Should be 8
    print(subtract(10, 4))  # Should be 6
    print(multiply(3, 7))   # Should be 21
    print(divide(15, 3))    # Should be 5.0
    print(power(2, 3))      # Should be 8