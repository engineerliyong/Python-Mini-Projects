# Calculator with History 🧮

**Project 04** of 30 Python Mini Projects

An interactive command-line calculator that performs basic arithmetic operations and maintains a complete history of all calculations with timestamps.

## Features

- ✅ **Basic Arithmetic** - Addition, subtraction, multiplication, division, power
- ✅ **Calculation History** - Tracks all calculations with timestamps
- ✅ **View History** - Display all previous calculations
- ✅ **Clear History** - Remove all calculations with confirmation
- ✅ **Save to File** - Export history to text file
- ✅ **Load from File** - View saved history reports
- ✅ **Error Handling** - Prevents division by zero, validates input
- ✅ **Menu-Driven Interface** - Easy navigation with numbered options
- ✅ **Auto-Save Prompt** - Asks to save before exiting

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

### Main Menu
```
======================================================================
  CALCULATOR WITH HISTORY
======================================================================
1. Perform calculation
2. View history
3. Clear history
4. Save history to file
5. Load history from file
6. Exit
======================================================================

Enter choice (1-6):
```

### Example Session

#### **Performing Calculations**
```
Enter choice (1-6): 1

----------------------------------------------------------------------
  NEW CALCULATION
----------------------------------------------------------------------
Enter first number: 25
Operations: + (add), - (subtract), * (multiply), / (divide), ** (power)
Enter operation: *
Enter second number: 4

----------------------------------------------------------------------
  25.0 * 4.0 = 100.0
----------------------------------------------------------------------
```

#### **Viewing History**
```
Enter choice (1-6): 2

======================================================================
  CALCULATION HISTORY
======================================================================
  1. [2026-01-09 14:30:15] 25.0 * 4.0 = 100.0
  2. [2026-01-09 14:31:22] 50.0 + 30.0 = 80.0
  3. [2026-01-09 14:32:45] 100.0 / 5.0 = 20.0
======================================================================
Total calculations: 3
```

#### **Saving History**
```
Enter choice (1-6): 4

Enter filename [history.txt]: my_calculations.txt

✓ History saved to: my_calculations.txt
```

#### **Division by Zero Handling**
```
Enter first number: 10
Enter operation: /
Enter second number: 0

----------------------------------------------------------------------
  10.0 / 0.0 = Error: Division by zero
----------------------------------------------------------------------
```

## Code Structure

### Functions Overview

**Arithmetic Operations:**
- `add(a, b)` - Addition
- `subtract(a, b)` - Subtraction
- `multiply(a, b)` - Multiplication
- `divide(a, b)` - Division (with zero-check)
- `power(a, b)` - Exponentiation

**History Management:**
- `add_to_history(expression, result)` - Stores calculation with timestamp
- `view_history()` - Displays all calculations
- `clear_history()` - Removes all history (with confirmation)
- `save_history(filename)` - Exports to text file
- `load_history(filename)` - Reads saved history

**User Interface:**
- `display_menu()` - Shows main menu
- `perform_calculation()` - Handles calculation workflow
- `get_number(prompt)` - Input validation for numbers
- `get_operation()` - Input validation for operations
- `main()` - Main program loop

### Data Structure

**History Storage:**
```python
calculation_history = [
    {
        'timestamp': '2026-01-09 14:30:15',
        'expression': '25.0 * 4.0',
        'result': 100.0
    },
    # ... more entries
]
```

### Program Flow
```
1. Display menu
   ↓
2. Get user choice
   ↓
3. Execute chosen action:
   - Perform calculation
   - View history
   - Clear history
   - Save to file
   - Load from file
   - Exit
   ↓
4. Loop back to menu (unless exit chosen)
```

## What I Learned

### Python Concepts

#### 1. **Lists for Data Storage**
```python
calculation_history = []  # Initialize empty list
calculation_history.append(entry)  # Add item
len(calculation_history)  # Count items

# Check if empty
if not calculation_history:
    print("No history!")
```
- Lists are mutable and ordered
- Perfect for storing sequential data
- Can hold any data type (strings, dicts, numbers)

#### 2. **While Loops for Menus**
```python
while True:
    display_menu()
    choice = input("Enter choice: ")
    
    if choice == '6':
        break  # Exit loop
    
    # Process choice
```
- `while True` creates infinite loop
- `break` exits the loop
- Great for menu systems

#### 3. **Global Variables**
```python
calculation_history = []  # Global variable

def clear_history():
    global calculation_history  # Declare we're modifying global
    calculation_history = []  # Reset to empty list
```
- Used when multiple functions need access to same data
- Must use `global` keyword to modify
- Alternative: use classes or pass as parameters

#### 4. **Datetime Module**
```python
import datetime

now = datetime.datetime.now()
# datetime.datetime(2026, 1, 9, 14, 30, 15)

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
# "2026-01-09 14:30:15"
```
- `strftime()` formats dates as strings
- `%Y` = 4-digit year, `%m` = month, `%d` = day
- `%H` = hour (24h), `%M` = minute, `%S` = second

#### 5. **Input Validation with Try-Except**
```python
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Try again.")
```
- Keeps asking until valid input received
- `try-except` catches errors gracefully
- Better UX than crashing

#### 6. **String Methods**
```python
operation = input("Enter operation: ").strip()
# Removes leading/trailing whitespace

answer = input("Save? (y/n): ").strip().lower()
# Chains methods: strip THEN lowercase
```
- `.strip()` removes whitespace
- `.lower()` converts to lowercase
- Can chain methods together

#### 7. **Dictionaries for Structured Data**
```python
entry = {
    'timestamp': '2026-01-09 14:30:15',
    'expression': '25.0 * 4.0',
    'result': 100.0
}

# Access values
print(entry['timestamp'])
print(entry['result'])
```
- Key-value pairs
- Self-documenting (keys describe data)
- Easy to extend (add new keys)

#### 8. **File I/O**
```python
# Writing
with open('history.txt', 'w', encoding='utf-8') as f:
    f.write("Data here\n")

# Reading
with open('history.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```
- `with` statement auto-closes file
- `'w'` = write mode (overwrites)
- `'r'` = read mode
- Always use `encoding='utf-8'`

### Key Takeaways

✅ **Lists are perfect for collections** - Much better than 100+ variables  
✅ **Input validation prevents crashes** - Always validate user input  
✅ **Dictionaries organize related data** - Better than separate variables  
✅ **While loops power menus** - Combined with `break` for exit  
✅ **Global variables need care** - Must declare with `global` keyword  
✅ **String methods are powerful** - `.strip()` and `.lower()` improve UX  
✅ **Timestamps add professionalism** - Users appreciate detailed records

## Challenges & Solutions

### Challenge 1: Managing History Data
**Problem**: How to store multiple calculations with different data types (timestamp, expression, result)?

**First attempt**: Separate lists
```python
timestamps = []
expressions = []
results = []
# Hard to keep synchronized!
```

**Solution**: List of dictionaries
```python
calculation_history = [
    {'timestamp': '...', 'expression': '...', 'result': ...}
]
# All related data stays together ✓
```

**Lesson**: Dictionaries are perfect for structured records.

---

### Challenge 2: Division by Zero
**Problem**: Calculator crashes when dividing by zero

**Solution**: Check before dividing
```python
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
```

**Lesson**: Always validate mathematical operations.

---

### Challenge 3: Invalid User Input
**Problem**: Program crashes when user enters text instead of number

**First attempt**: Basic check
```python
num = input("Enter number: ")
if not num.isdigit():  # ❌ Fails for decimals and negatives
    print("Error")
```

**Solution**: Try-except loop
```python
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Try again.")
```

**Lesson**: Try-except is better for type conversion validation.

---

### Challenge 4: Clearing Global List
**Problem**: `clear_history()` creates local variable instead of modifying global

**Broken code**:
```python
def clear_history():
    calculation_history = []  # Creates LOCAL variable!
    # Global list unchanged ❌
```

**Solution**: Use `global` keyword
```python
def clear_history():
    global calculation_history
    calculation_history = []  # Modifies GLOBAL ✓
```

**Lesson**: Must declare `global` when reassigning global variables.

---

### Challenge 5: Accidental Whitespace in Input
**Problem**: User types " + " (with spaces) and operation doesn't match

**Solution**: Use `.strip()`
```python
operation = input("Enter operation: ").strip()
# "  +  " becomes "+"
```

**Lesson**: Always `.strip()` user input for single-value entries.

---

### Challenge 6: Formatting Timestamps
**Problem**: Default datetime format is ugly
```python
datetime.datetime.now()
# 2026-01-09 14:30:15.123456
```

**Solution**: Custom format with strftime
```python
now.strftime("%Y-%m-%d %H:%M:%S")
# "2026-01-09 14:30:15"
```

**Lesson**: `strftime()` gives full control over date formatting.

## Sample Output

### Saved History File (history.txt)
```
======================================================================
  CALCULATOR HISTORY REPORT
======================================================================

1. [2026-01-09 14:30:15] 25.0 * 4.0 = 100.0
2. [2026-01-09 14:31:22] 50.0 + 30.0 = 80.0
3. [2026-01-09 14:32:45] 100.0 / 5.0 = 20.0
4. [2026-01-09 14:33:12] 2.0 ** 8.0 = 256.0
5. [2026-01-09 14:34:01] 100.0 - 37.0 = 63.0

======================================================================
Total calculations: 5
======================================================================
```

## Testing

### Test Cases Performed
```
✅ Test 1: Addition (5 + 3 = 8)
✅ Test 2: Subtraction (10 - 4 = 6)
✅ Test 3: Multiplication (7 * 8 = 56)
✅ Test 4: Division (100 / 4 = 25.0)
✅ Test 5: Power (2 ** 10 = 1024)
✅ Test 6: Division by zero (handled with error message)
✅ Test 7: Invalid number input ("abc" → re-prompt)
✅ Test 8: Invalid operation ("x" → re-prompt)
✅ Test 9: View empty history (shows "No history" message)
✅ Test 10: Clear history (asks confirmation)
✅ Test 11: Save history to file (creates file)
✅ Test 12: Load history from file (displays content)
✅ Test 13: Custom filename (works correctly)
✅ Test 14: Exit with unsaved history (prompts to save)
✅ Test 15: Multiple calculations in one session
```

### Edge Cases Handled
- Empty history (all operations check first)
- Division by zero (returns error message)
- Invalid numeric input (keeps asking)
- Invalid operation (keeps asking)
- Missing file when loading (shows error)
- Whitespace in input (stripped)
- Decimal numbers (accepted)
- Negative numbers (accepted)
- Very large numbers (handled)

## Future Improvements

### Version 2.0
- [ ] Add square root operation
- [ ] Add modulo (%) operation
- [ ] Add factorial operation
- [ ] Support negative numbers better

### Version 3.0
- [ ] Accept full expressions: "5 + 3 * 2"
- [ ] Parentheses support: "(5 + 3) * 2"
- [ ] Variables: store results as x, y, z
- [ ] Last answer reference: "ANS + 5"

### Version 4.0
- [ ] Export to CSV format
- [ ] Statistics: most-used operation, average result
- [ ] Search history by date or operation
- [ ] Undo last calculation
- [ ] Memory functions (M+, M-, MR, MC)

### Version 5.0
- [ ] GUI with tkinter
- [ ] Graphing capabilities
- [ ] Scientific functions (sin, cos, tan, log)
- [ ] Unit conversions
- [ ] Currency conversions (with API)

## Project Statistics

| Metric | Value |
|--------|-------|
| **Lines of Code** | ~280 |
| **Functions** | 12 |
| **Time to Complete** | ~3 hours |
| **Difficulty** | ⭐⭐ Intermediate |
| **Date Completed** | January 2026 |

### Time Breakdown
- Planning & design: 20 minutes
- Basic operations: 30 minutes
- History management: 45 minutes
- Menu system: 40 minutes
- File I/O: 25 minutes
- Testing & debugging: 40 minutes
- Documentation: 20 minutes

## Comparison with Previous Projects

| Aspect | Project 02 | Project 03 | Project 04 |
|--------|------------|------------|------------|
| **Data Structure** | Counter | DataFrame | List of Dicts |
| **User Input** | File path | File path | Multiple inputs |
| **Loop Type** | None | None | While loop |
| **Global State** | No | No | Yes (history) |
| **External Libs** | collections | pandas | None (stdlib) |
| **Complexity** | Medium | Medium-High | Medium |

### Evolution from Project 03
- **Menu-driven interface** vs single-run analysis
- **Global state management** (history list)
- **Interactive loop** with multiple options
- **More complex user interaction** (multiple inputs per action)
- **Datetime usage** for timestamps
- **Confirmation prompts** (before clearing, exiting)

## Dependencies

**Standard Library Only:**
- `datetime` - Timestamps
- Built-in functions - Input/output, file operations

**No `pip install` required!** ✨

## Files

```
project-04-calculator/
├── calculator.py          # Main program
├── README.md             # This file
├── history.txt           # Generated by save function
└── .gitignore            # Ignore history files
```

## Reflection

### What I'm Proud Of
- **Clean menu system** - Easy to navigate and understand
- **Comprehensive error handling** - Validates all user input
- **Timestamps in history** - Professional touch
- **Confirmation prompts** - Prevents accidental data loss
- **Save-before-exit feature** - Good UX practice
- **No external dependencies** - Uses only Python standard library

### What I Struggled With
- **Global variable management** - Forgot `global` keyword initially
- **Input validation loop** - Took a few tries to get right
- **File formatting** - Making saved reports look professional
- **Menu flow** - Deciding when to prompt for input

### How I Improved from Project 03
- **Interactive vs single-run** - Added menu loop for continuous use
- **State management** - Learned to work with global variables
- **Better UX** - Confirmation prompts, save-before-exit
- **More complex control flow** - While loops, multiple user paths
- **Cleaner code organization** - More small, focused functions

### Key Lessons

1. **User input needs LOTS of validation** - Can never be too careful
2. **Global variables are convenient but need discipline** - Easy to misuse
3. **Timestamps make history valuable** - Users appreciate detailed records
4. **Confirmation prompts prevent regret** - Before destructive actions
5. **Menu systems need clear exit paths** - Easy to trap users in loops
6. **`.strip()` is your friend** - Handles user mistakes gracefully
7. **While True + break = menu loop** - Simple but effective pattern

## Usage Tips

### Best Practices
- **Clear history regularly** - Keeps display manageable
- **Save before clearing** - Preserve important calculations
- **Use descriptive filenames** - "monthly_budget.txt" vs "history.txt"
- **Check history before exiting** - Don't lose work

### Common Mistakes to Avoid
- Entering "plus" instead of "+"
- Forgetting to save before clearing
- Using comma as decimal separator (use period)

## Resources Used

- [Python datetime documentation](https://docs.python.org/3/library/datetime.html)
- [Python file I/O guide](https://docs.python.org/3/tutorial/inputoutput.html)
- [Global vs local variables](https://realpython.com/python-scope-legb-rule/)
- Stack Overflow for input validation patterns

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

*Learning Python one project at a time* 🚀
