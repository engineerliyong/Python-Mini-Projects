# Temperature Converter 🌡️

**Project 01** of 30 Python Mini Projects

A simple command-line temperature converter that converts between Celsius and Fahrenheit with input validation and absolute zero checking.

## 📋 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Code Structure](#-code-structure)
- [What I Learned](#-what-i-learned)
- [Challenges & Solutions](#-challenges--solutions)
- [Future Improvements](#-future-improvements)
- [Testing](#-testing)

## ✨ Features

- ✅ **Bidirectional Conversion**: Celsius ↔ Fahrenheit
- ✅ **Input Validation**: Handles user input with `.strip()` and `.upper()`
- ✅ **Absolute Zero Check**: Prevents conversion of physically impossible temperatures
- ✅ **Clean Output**: Formatted temperature display with degree symbols
- ✅ **User-Friendly**: Clear prompts and error messages

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher

### Setup
```bash
# Clone the main repository
git clone https://github.com/engineerliyong/python-mini-projects.git

# Navigate to this project
cd python-mini-projects/project-01-temp-converter

# No additional dependencies required!
```

## 💻 Usage

### Basic Usage
```bash
python temp_converter.py
```

### Example Session
```
Enter temperature to convert: 
25
Enter units (C for Celsius, F for Fahrenheit): 
C
25.0°C is 77.0°F
```

### Another Example
```
Enter temperature to convert: 
98.6
Enter units (C for Celsius, F for Fahrenheit): 
F
98.6°F is 37.0°C
```

### Error Handling Example
```
Enter temperature to convert: 
-500
Enter units (C for Celsius, F for Fahrenheit): 
C
Error: Temperature below absolute zero in Celsius.
```

## 🏗️ Code Structure

### Functions

**`celsius_to_fahrenheit(celsius)`**
- Converts Celsius to Fahrenheit using the formula: `F = (C × 9/5) + 32`
- **Parameters**: `celsius` (float) - Temperature in Celsius
- **Returns**: (float) - Temperature in Fahrenheit

**`fahrenheit_to_celsius(fahrenheit)`**
- Converts Fahrenheit to Celsius using the formula: `C = (F - 32) × 5/9`
- **Parameters**: `fahrenheit` (float) - Temperature in Fahrenheit
- **Returns**: (float) - Temperature in Celsius

### Main Program Flow
```
1. Prompt user for temperature (number)
2. Prompt user for units (C or F)
3. Validate input:
   - Check if temperature is above absolute zero
4. Convert temperature using appropriate function
5. Display result with proper formatting
```

### Validation Rules
- **Celsius**: Must be ≥ -273.15°C (absolute zero)
- **Fahrenheit**: Must be ≥ -459.67°F (absolute zero)
- **Units**: Must be 'C' or 'F' (case-insensitive)

## 📚 What I Learned

### Python Concepts Applied

#### 1. **Functions with Docstrings**
```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
```
- Learned to write clear, reusable functions
- Used docstrings for documentation

#### 2. **User Input Handling**
```python
temp = float(input())
units = input().strip().upper()
```
- `float()` for type conversion
- `.strip()` to remove whitespace
- `.upper()` for case-insensitive comparison

#### 3. **Conditional Logic**
```python
if units == 'C':
    if temp < -273.15:
        print("Error: Temperature below absolute zero")
    else:
        converted = celsius_to_fahrenheit(temp)
```
- Nested conditionals for validation
- Using `if-elif-else` for multiple conditions

#### 4. **String Formatting**
```python
print(f"{temp}°C is {converted}°F")
```
- F-strings for readable output
- Unicode characters (°) in strings

### Key Takeaways

✅ **Validation is crucial**: Always check user input before processing  
✅ **Edge cases matter**: Absolute zero is a real physical constraint  
✅ **Code reusability**: Functions make code cleaner and testable  
✅ **User experience**: Clear prompts and error messages improve usability

## 🐛 Challenges & Solutions

### Challenge 1: Invalid Input Handling
**Problem**: Program crashes when user enters non-numeric input (e.g., "abc")

**Current Status**: ⚠️ Not yet handled

**Planned Solution**:
```python
try:
    temp = float(input("Enter temperature: "))
except ValueError:
    print("Error: Please enter a valid number")
```

### Challenge 2: Incorrect Conversion on Error
**Problem**: Initially, the program would convert temperature even when below absolute zero

**Solution**: ✅ Fixed by adding `else` clause
```python
if temp < -273.15:
    print("Error: Temperature below absolute zero")
else:
    converted = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is {converted}°F")
```

### Challenge 3: Invalid Unit Input
**Problem**: If user enters 'X' or any invalid unit, program outputs nothing

**Current Status**: ⚠️ Silent failure - no error message

**Planned Solution**: Add `else` clause to catch invalid units
```python
elif units == 'F':
    # conversion code
else:
    print("Error: Please enter 'C' or 'F'")
```

## 🔮 Future Improvements

### Immediate Improvements (V2)
- [ ] Add `try-except` for ValueError handling
- [ ] Add `else` clause for invalid unit input
- [ ] Add option to convert another temperature
- [ ] Format output to 1 decimal place (`.1f`)

### Advanced Features (V3)
- [ ] Support Kelvin conversion
- [ ] Support Rankine scale
- [ ] Command-line arguments: `python temp_converter.py 25 C`
- [ ] Batch conversion from file
- [ ] Save conversion history to CSV

### Bonus Features (V4)
- [ ] GUI with tkinter
- [ ] Web interface with Flask
- [ ] Temperature conversion table generator
- [ ] Unit tests with pytest

## 🧪 Testing

### Manual Tests Performed
```
✅ Test 1: 0°C → 32°F (Passed)
✅ Test 2: 100°C → 212°F (Passed)
✅ Test 3: 32°F → 0°C (Passed)
✅ Test 4: 98.6°F → 37°C (Passed)
✅ Test 5: -273.15°C → Error (Passed)
✅ Test 6: -459.67°F → Error (Passed)
⚠️ Test 7: "abc" input → Crashes (Needs fix)
⚠️ Test 8: "X" for units → Silent failure (Needs fix)
```

### Test Cases to Add
```python
# When implementing automated tests
assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212
assert fahrenheit_to_celsius(32) == 0
assert fahrenheit_to_celsius(212) == 100
assert round(fahrenheit_to_celsius(98.6), 1) == 37.0
```

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| **Lines of Code** | ~30 |
| **Functions** | 2 |
| **Time to Complete** | ~70 minutes |
| **Difficulty** | ⭐ Beginner |
| **Date Completed** | January 8, 2026 |

### Time Breakdown
- Planning & Setup: 10 minutes
- Writing Code: 30 minutes
- Testing & Debugging: 15 minutes
- Documentation: 15 minutes

## 🔗 Related Files

- **Main Code**: [`temp_converter.py`](./temp_converter.py)
- **Tests**: `Coming soon`
- **Version 2**: `Coming soon` (with improvements)

## 📖 Lessons for Next Project

**What worked well:**
- Clear function names and docstrings
- Checking for absolute zero (edge case thinking)
- Using `.strip()` and `.upper()` for robust input

**What needs improvement:**
- Error handling with try-except
- More comprehensive validation
- Better code organization (main function)
- Automated testing

**Apply to Project 02:**
- Implement try-except from the start
- Write tests alongside code
- Use `if __name__ == "__main__"` pattern
- Add more detailed comments

## 🎯 Next Project

**Project 02: File Word Counter**

Will focus on:
- File I/O operations
- Dictionary usage
- String manipulation
- Sorting and filtering data

## 🤝 Contributing

This is a learning project, but feedback is welcome!

If you have suggestions:
1. Open an issue in the [main repository](https://github.com/engineerliyong/python-mini-projects/issues)
2. Describe the improvement
3. Tag it with `project-01`

## 📝 Reflection

### What I'm Proud Of
- Clean, readable code
- Thinking about physical constraints (absolute zero)
- Good documentation with docstrings

### What I Struggled With
- Remembering to validate BEFORE conversion
- Realizing the silent failure with invalid units
- Balancing features vs. simplicity

### How I'll Improve
- Test edge cases earlier in development
- Write error handling first, not as an afterthought
- Create a checklist of validations before coding

---

**Part of**: [30 Python Mini Projects](https://github.com/engineerliyong/python-mini-projects)  
**Author**: [Liza Bambu](https://github.com/engineerliyong)  
**Date**: January 8, 2026  
**Status**: ✅ Complete (V1) | 🔄 Improvements Planned (V2)

---

## 📚 References

- [Python Official Documentation](https://docs.python.org/3/)
- [Temperature Conversion Formulas](https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature)
- [Absolute Zero](https://en.wikipedia.org/wiki/Absolute_zero)

---

*Learning Python one project at a time* 🚀