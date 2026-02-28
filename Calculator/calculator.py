"""
Calculator with History
Author: Liza Bambu
Date: January 2026
Interactive calculator that tracks calculation history.
"""
import datetime

# Global list to store history
calculation_history = []


def add(a, b):
    """Add two numbers"""
    added_value = a + b
    return added_value


def subtract(a, b):
    """Subtract b from a"""
    subtracted_value = a - b
    return subtracted_value


def multiply(a, b):
    """Multiply two numbers"""
    multiplied_value = a * b
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
    """Get a valid number from user"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_operation():
    """Get a valid operation from user"""
    valid_operations = ['+', '-', '*', '/', '**']
    
    while True:
        print("\nOperation: + (Add), - (Subtract), * (Multiply), / (Divide), ** (Power)")
        operation = input("Enter operation: ").strip()
        
        if operation in valid_operations:
            return operation
        else:
            print(f"Invalid operation. Please choose from: {', '.join(valid_operations)}")


def perform_operation(a, operation, b):
    """Perform the calculation based on operation"""
    if operation == '+':
        return add(a, b)
    elif operation == '-':
        return subtract(a, b)
    elif operation == '*':
        return multiply(a, b)
    elif operation == '/':
        return divide(a, b)
    elif operation == '**':
        return power(a, b)


def add_to_history(expression, result):
    """Add calculation to history"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {expression} = {result}"
    calculation_history.append(entry)


def view_history():
    """Display all calculation history"""
    if not calculation_history:
        print("\nNo calculation history yet!")
        return
    
    print("\n" + "=" * 60)
    print("  CALCULATION HISTORY")
    print("=" * 60)
    for i, entry in enumerate(calculation_history, 1):
        print(f"{i}. {entry}")
    print("=" * 60)
    print(f"Total calculations: {len(calculation_history)}")


def clear_history():
    """Clear all calculation history"""
    global calculation_history
    
    if not calculation_history:
        print("\nHistory is already empty!")
        return
    
    confirm = input(f"\nClear {len(calculation_history)} calculation(s)? (y/n): ").strip().lower()
    
    if confirm == 'y':
        calculation_history = []
        print("✓ History cleared!")
    else:
        print("Clear cancelled.")


def save_history(filename="history.txt"):
    """Save calculation history to file"""
    if not calculation_history:
        print("\nNo history to save!")
        return
    
    try:
        with open(filename, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("  CALCULATOR HISTORY\n")
            f.write("=" * 60 + "\n\n")
            
            for i, entry in enumerate(calculation_history, 1):
                f.write(f"{i}. {entry}\n")
            
            f.write("\n" + "=" * 60 + "\n")
            f.write(f"Total calculations: {len(calculation_history)}\n")
        
        print(f"\n✓ History saved to: {filename}")
    
    except Exception as e:
        print(f"\nError saving history: {e}")


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 60)
    print("  CALCULATOR WITH HISTORY")
    print("=" * 60)
    print("1. Perform calculation")
    print("2. View history")
    print("3. Clear history")
    print("4. Save history to file")
    print("5. Exit")
    print("=" * 60)


def perform_calculation():
    """Get input and perform calculation"""
    print("\n" + "-" * 60)
    print("  NEW CALCULATION")
    print("-" * 60)
    
    # Get numbers and operation
    num1 = get_number("Enter first number: ")
    operation = get_operation()
    num2 = get_number("Enter second number: ")
    
    # Calculate
    result = perform_operation(num1, operation, num2)
    
    # Create expression
    expression = f"{num1} {operation} {num2}"
    
    # Display result
    print("\n" + "-" * 60)
    print(f"  Result: {expression} = {result}")
    print("-" * 60)
    
    # Add to history (only if not an error)
    if not isinstance(result, str):
        add_to_history(expression, result)


def main():
    """Main function with menu loop"""
    print("\n" + "=" * 60)
    print("  WELCOME TO CALCULATOR WITH HISTORY")
    print("=" * 60)
    
    while True:
        display_menu()
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            perform_calculation()
        
        elif choice == '2':
            view_history()
        
        elif choice == '3':
            clear_history()
        
        elif choice == '4':
            filename = input("Enter filename [history.txt]: ").strip()
            if not filename:
                filename = "history.txt"
            save_history(filename)
        
        elif choice == '5':
            # Ask to save before exit
            if calculation_history:
                save_before_exit = input("\nSave history before exiting? (y/n): ").strip().lower()
                if save_before_exit == 'y':
                    save_history()
            
            print("\nThank you for using Calculator!")
            print("Goodbye! 👋\n")
            break
        
        else:
            print("\nInvalid choice. Please enter 1-5.")


if __name__ == "__main__":
    # Test functions (comment out when running main program)
    # print(add(5, 3))        # Should be 8
    # print(subtract(10, 4))  # Should be 6
    # print(multiply(3, 7))   # Should be 21
    # print(divide(15, 3))    # Should be 5.0
    # print(power(2, 3))      # Should be 8
    
    # Run main program
    main()
