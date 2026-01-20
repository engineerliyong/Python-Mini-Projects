# Calculator with History 🧮

**Project 04** of 30 Python Mini Projects

An interactive command-line calculator that performs basic arithmetic operations and maintains a complete history of all calculations with timestamps.

## Features

- ✅ **Basic Operations** - Addition, Subtraction, Multiplication, Division, Power
- ✅ **Calculation History** - Tracks all calculations with timestamps
- ✅ **View History** - Display all past calculations
- ✅ **Clear History** - Remove all saved calculations (with confirmation)
- ✅ **Save to File** - Export calculation history to text file
- ✅ **Error Handling** - Division by zero protection and input validation
- ✅ **Menu-Driven Interface** - Easy-to-use interactive menu
- ✅ **Auto-Save on Exit** - Option to save history before closing

## Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies (uses standard library only)

### Setup
```bash
# Clone the repository
git clone https://github.com/engineerliyong/python-mini-projects.git

# Navigate to this project
cd python-mini-projects/project-04-calculator

# Run the calculator
python calculator.py
```

## Usage

### Starting the Calculator
```bash
python calculator.py
```

### Example Session
```
======================================================================
  WELCOME TO CALCULATOR WITH HISTORY
======================================================================

======================================================================
  CALCULATOR WITH HISTORY
======================================================================
1. Perform calculation
2. View history
3. Clear history
4. Save history to file
5. Exit
======================================================================

Enter choice (1-5): 1

----------------------------------------------------------------------
  NEW CALCULATION
----------------------------------------------------------------------
Enter first number: 15
Operation: + (Add), - (Subtract), * (Multiply), / (Divide), ** (Power)
Enter operation: +
Enter second number: 7

----------------------------------------------------------------------
  Result: 15.0 + 7.0 = 22.0
----------------------------------------------------------------------

Enter choice (1-5): 2

======================================================================
  CALCULATION HISTORY
======================================================================
1. [2026-01-09 15:30:45] 15.0 + 7.0 = 22.0
======================================================================
Total calculations: 1
```

### Menu Options

**1. Perform Calculation**
- Enter first number
- Choose operation (+, -, *, /, **)
- Enter second number
- View result and automatic history save

**2. View History**
- Displays all calculations with timestamps
- Shows total number of calculations

**3. Clear History**
- Asks for confirmation before clearing
- Removes all saved calculations

**4. Save History to File**
- Saves complete history to text file
- Default filename: `history.txt`
- Custom filename supported

**5. Exit**
- Option to save history before closing
- Clean exit with goodbye message

## Code Structure

### Functions Overview

**Basic Operations:**
```python
add(a, b)         # Returns a + b
subtract(a, b)    # Returns a - b
multiply(a, b)    # Returns a * b
divide(a, b)      # Returns a / b (handles division by zero)
power(a, b)       # Returns a ** b
```

**Input Handling:**
```python
get_number(prompt)      # Gets valid number from user with error handling
get_operation()         # Gets valid operation symbol (+, -, *, /, **)
perform_operation(a, op, b)  # Executes the appropriate operation
```

**History Management:**
```python
add_to_history(expression, result)  # Adds calculation with timestamp
view_history()                       # Displays all calculations
clear_history()                      # Clears all history (with confirmation)
save_history(filename)               # Saves history to text file
```

**Program Flow:**
```python
display_menu()           # Shows menu options
perform_calculation()    # Handles one calculation cycle
main()                   # Main loop with menu system
```

### Data Structure

**History Storage:**
```python
calculation_history = [
    "[2026-01-09 15:30:45] 15.0 + 7.0 = 22.0",
    "[2026-01-09 15:31:02] 20.0 * 3.0 = 60.0",
    "[2026-01-09 15:31:18] 100.0 / 4.0 = 25.0"
]
```

## What I Learned

### Python Concepts

#### 1. **Lists for Data Storage**
```python
calculation_history = []           # Initialize empty list
calculation_history.append(item)   # Add item to list
len(calculation_history)           # Get list length
for entry in calculation_history:  # Loop through list
```
- Lists are mutable and perfect for storing sequences
- Can easily add, remove, and iterate over items
- Length checking with `len()` for conditional logic

#### 2. **While Loops for Continuous Execution**
```python
while True:
    # Menu loop - runs until break
    choice = input("Enter choice: ")
    if choice == '5':
        break  # Exit loop
```
- `while True` creates infinite loop for menus
- `break` statement exits the loop
- Perfect for interactive programs

#### 3. **Input Validation with Try-Except**
```python
while True:
    try:
        value = float(input("Enter number: "))
        return value  # Valid input, exit loop
    except ValueError:
        print("Invalid input. Try again.")
        # Loop continues
```
- `try-except` handles errors gracefully
- `ValueError` catches non-numeric input
- Loop continues until valid input received

#### 4. **DateTime Module**
```python
import datetime
timestamp = datetime.datetime.now()
formatted = timestamp.strftime("%Y-%m-%d %H:%M:%S")
# Output: "2026-01-09 15:30:45"
```
- `datetime.now()` gets current date and time
- `strftime()` formats datetime as string
- Custom format strings for different displays

#### 5. **Global Variables**
```python
calculation_history = []  # Global variable

def clear_history():
    global calculation_history  # Modify global variable
    calculation_history = []
```
- `global` keyword allows function to modify global variables
- Useful for shared state across functions
- Must declare before assignment

#### 6. **String Formatting**
```python
# F-strings for readable formatting
expression = f"{num1} {operation} {num2}"
entry = f"[{timestamp}] {expression} = {result}"

# Output: "[2026-01-09 15:30:45] 15.0 + 7.0 = 22.0"
```
- F-strings provide clean variable interpolation
- Can include expressions inside `{}`
- More readable than concatenation or `.format()`

#### 7. **File Writing**
```python
with open(filename, 'w') as f:
    f.write("Text to write\n")
    f.write(f"Variable: {value}\n")
# File automatically closes
```
- `with` statement ensures file closes properly
- `'w'` mode overwrites file (use `'a'` to append)
- `\n` for newlines

### Key Takeaways

✅ **Input validation is essential** - Never trust user input  
✅ **Lists are powerful** - Easy to store and manipulate sequences  
✅ **While loops for menus** - Clean way to create interactive programs  
✅ **Global variables have their place** - Shared state across functions  
✅ **Error messages should guide users** - Tell them what went wrong and how to fix it  
✅ **Timestamps add context** - Makes history more useful

## Challenges & Solutions

### Challenge 1: Division by Zero
**Problem**: Program crashes when dividing by zero

**Solution**: 
```python
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
```
Added check before division and return error message instead of crashing.

### Challenge 2: Invalid Input Handling
**Problem**: Non-numeric input causes `ValueError`

**Solution**:
```python
def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
```
Used try-except to catch errors and loop until valid input received.

### Challenge 3: Modifying Global List
**Problem**: Clearing history inside function didn't work

**Solution**:
```python
def clear_history():
    global calculation_history  # Must declare global
    calculation_history = []
```
Needed `global` keyword to reassign the global variable.

### Challenge 4: Saving History Format
**Problem**: History file was hard to read

**Solution**:
```python
f.write("=" * 60 + "\n")  # Header separator
f.write(f"{i}. {entry}\n")  # Numbered entries
f.write(f"Total calculations: {len(calculation_history)}\n")
```
Added formatting with separators, numbering, and summary.

### Challenge 5: Preventing Accidental Data Loss
**Problem**: Users might exit without saving

**Solution**:
```python
if calculation_history:
    save_before_exit = input("Save history before exiting? (y/n): ")
    if save_before_exit == 'y':
        save_history()
```
Added prompt before exit to save unsaved work.

## Sample Output Files

### history.txt Format
```
============================================================
  CALCULATOR HISTORY
============================================================

1. [2026-01-09 15:30:45] 15.0 + 7.0 = 22.0
2. [2026-01-09 15:31:02] 20.0 * 3.0 = 60.0
3. [2026-01-09 15:31:18] 100.0 / 4.0 = 25.0
4. [2026-01-09 15:31:35] 2.0 ** 8.0 = 256.0
5. [2026-01-09 15:31:50] 50.0 - 12.0 = 38.0

============================================================
Total calculations: 5
```

## Testing

### Test Cases
```
✅ Test 1: Addition (5 + 3 = 8) - Passed
✅ Test 2: Subtraction (10 - 4 = 6) - Passed
✅ Test 3: Multiplication (3 * 7 = 21) - Passed
✅ Test 4: Division (15 / 3 = 5.0) - Passed
✅ Test 5: Power (2 ** 3 = 8) - Passed
✅ Test 6: Division by zero - Error handled correctly
✅ Test 7: Invalid number input - Error handled, asks again
✅ Test 8: Invalid operation - Error handled, asks again
✅ Test 9: View empty history - Shows "No history yet"
✅ Test 10: Clear history with confirmation - Works correctly
✅ Test 11: Save history to file - File created successfully
✅ Test 12: Exit without saving - Prompts to save
```

### Edge Cases Handled
- Division by zero (returns error message)
- Non-numeric input (loops until valid)
- Invalid operation symbols (asks again)
- Empty history (appropriate messages)
- File save errors (try-except handling)
- Accidental spaces in input (`.strip()`)

## Future Improvements

### Version 2.0 (Planned)
- [ ] More operations (square root, modulo, factorial)
- [ ] Memory functions (M+, M-, MR, MC)
- [ ] Expression parsing (calculate "5 + 3 * 2" directly)
- [ ] Undo last calculation
- [ ] Edit/delete specific history entries

### Version 3.0 (Advanced)
- [ ] Scientific calculator mode (sin, cos, tan, log)
- [ ] Unit conversions (temperature, length, weight)
- [ ] Currency conversion with live rates
- [ ] Graphing calculator features
- [ ] Export to CSV/Excel

### Version 4.0 (GUI)
- [ ] Tkinter GUI interface
- [ ] Button-based calculator
- [ ] Visual history panel
- [ ] Themes (light/dark mode)

## Project Statistics

| Metric | Value |
|--------|-------|
| **Lines of Code** | ~180 |
| **Functions** | 12 |
| **Time to Complete** | ~3 hours |
| **Difficulty** | ⭐⭐ Intermediate |
| **Date Completed** | January 2026 |

### Time Breakdown
- Understanding requirements: 15 minutes
- Basic operations: 30 minutes
- Input validation: 30 minutes
- History management: 45 minutes
- Menu system: 30 minutes
- File operations: 20 minutes
- Testing and debugging: 30 minutes
- Documentation: 30 minutes

## Comparison with Previous Projects

| Aspect | Project 01 | Project 02 | Project 03 | Project 04 |
|--------|------------|------------|------------|------------|
| **Data Structure** | Variables | Dict/Counter | DataFrame | Lists |
| **User Input** | Simple | File path | File path | Menu + numbers |
| **Loops** | None | For loops | Built-in | While loops |
| **File I/O** | None | Read/Write | Read | Write |
| **Error Handling** | Basic | Good | Excellent | Excellent |
| **Interactivity** | Low | Medium | Low | High |

### Evolution from Previous Projects
- **More interactive** - Menu-driven interface vs. single-run
- **State management** - Maintaining history across operations
- **Better UX** - Confirmations, save prompts, formatted output
- **Global variables** - First project using shared state
- **Loop control** - `while True` and `break` statements

## Useful Commands

```bash
# Run the calculator
python calculator.py

# Test individual functions (modify main to run tests)
python calculator.py

# Check if history file exists
ls -la history.txt  # Mac/Linux
dir history.txt     # Windows
```

## Dependencies

**Standard Library Only:**
- `datetime` - Timestamps for calculations
- Built-in functions - `input()`, `float()`, file operations

**No external packages required!** ✨

## Reflection

### What I'm Proud Of
- Clean menu-driven interface that's easy to use
- Comprehensive input validation - program never crashes
- Thoughtful user experience (save prompts, confirmations)
- Well-organized code with single-responsibility functions
- Proper error messages that guide the user

### What I Struggled With
- Understanding when to use `global` keyword
- Deciding between storing strings vs. dictionaries in history
- Formatting the menu to look professional
- Remembering to validate all user inputs
- Testing all edge cases thoroughly

### How I Improved from Project 03
- **More user interaction** - Menu vs. single analysis
- **State management** - History persists across operations
- **Better code organization** - More helper functions
- **Improved UX** - Confirmations and prompts
- **Loop mastery** - While loops for continuous operation

### Key Lessons Learned
1. **User experience matters** - Small touches like save prompts make a difference
2. **Validation everywhere** - Always validate user input
3. **Global variables** - Useful for shared state but use sparingly
4. **Menu design** - Clear options and feedback improve usability
5. **Error messages** - Be specific about what went wrong
6. **Testing is crucial** - Edge cases reveal bugs

## Links

- **Code**: [`calculator.py`](./calculator.py)
- **Sample History**: [`history.txt`](./history.txt)

## Resources Used

- [Python datetime module](https://docs.python.org/3/library/datetime.html)
- [Python lists documentation](https://docs.python.org/3/tutorial/datastructures.html)
- [File I/O guide](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- Stack Overflow for global variable questions

---

**Part of:** [30 Python Mini Projects](https://github.com/engineerliyong/python-mini-projects)  
**Author:** [Liza Bambu](https://github.com/engineerliyong)  
**Date:** January 2026  
**Status:** ✅ Complete  
**Next:** Project 05 - Password Generator & Validator

---

## Contributing

Found a bug or have a suggestion? Open an issue in the [main repository](https://github.com/engineerliyong/python-mini-projects/issues) and tag it with `project-04`.

---

*Building Python skills one project at a time* 🚀
