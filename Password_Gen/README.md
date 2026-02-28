# Password Generator & Validator 🔐

**Project 05** of 30 Python Mini Projects

A secure password generator and strength validator with customizable options and detailed feedback.

## Features

- ✅ **Password Generation** - Create random secure passwords
- ✅ **Customizable Options** - Choose character types (uppercase, lowercase, numbers, symbols)
- ✅ **Guaranteed Strength** - Ensures at least one of each selected character type
- ✅ **Password Validation** - Analyzes password strength with detailed feedback
- ✅ **Common Password Check** - Detects commonly used passwords
- ✅ **Visual Feedback** - Color-coded strength indicators with score bars
- ✅ **Generate & Validate** - Create and immediately analyze passwords
- ✅ **Menu Interface** - Easy-to-use interactive menu system

## Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies (uses standard library only)

### Setup
```bash
# Clone the repository
git clone https://github.com/engineerliyong/python-mini-projects.git

# Navigate to this project
cd python-mini-projects/project-05-password-gen

# Run the tool
python password_tool.py
```

## Usage

### Starting the Tool
```bash
python password_tool.py
```

### Example Session

**Generating a Password:**
```
============================================================
  PASSWORD GENERATOR & VALIDATOR
============================================================
1. Generate password
2. Validate password
3. Generate and validate
4. Exit
============================================================

Enter choice (1-4): 1

------------------------------------------------------------
  GENERATE PASSWORD
------------------------------------------------------------
Enter password length (minimum 8): 16
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y

------------------------------------------------------------
  Generated Password: K9$mPq2X@5TnLv
------------------------------------------------------------
  Length: 16 characters
  Uppercase: Yes
  Lowercase: Yes
  Numbers: Yes
  Special: Yes
------------------------------------------------------------
```

**Validating a Password:**
```
Enter choice (1-4): 2

------------------------------------------------------------
  VALIDATE PASSWORD
------------------------------------------------------------

Enter password to validate: MyPass123!

============================================================
  PASSWORD STRENGTH ANALYSIS
============================================================

Strength: 🟢 Strong
Score: 5/5
[█████]

Details:
  ✓ Length OK (8+ characters)
  ✓ Has uppercase letters
  ✓ Has lowercase letters
  ✓ Has numbers
  ✓ Has special characters
============================================================
```

## Code Structure

### Main Functions

**Password Generation:**
```python
generate_password(length, use_upper, use_lower, use_digits, use_special)
# Generates secure password with guaranteed character types
```

**Password Validation:**
```python
validate_password(password)
# Returns: {
#   "Length OK": bool,
#   "Has Uppercase": bool,
#   "Has Lowercase": bool,
#   "Has Digit": bool,
#   "Has Special": bool,
#   "Is Common": bool,
#   "Strength": "Weak"/"Medium"/"Strong",
#   "Score": int (0-5)
# }
```

**Input Validation:**
```python
get_password_length()
# Gets valid password length with error handling
```

**Display Functions:**
```python
display_validation_result(result)  # Shows formatted strength analysis
display_menu()                      # Shows main menu
```

**Menu Handlers:**
```python
handle_generate()              # Handles password generation
handle_validate()              # Handles password validation
handle_generate_and_validate() # Generates and validates in one step
```

### Program Flow
```
1. Display welcome message
   ↓
2. Show menu (loop)
   ↓
3. Get user choice
   ↓
4. Execute corresponding function
   ↓
5. Return to menu (or exit)
```

## What I Learned

### Python Concepts

#### 1. **String Module Constants**
```python
import string

string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
string.digits          # '0123456789'
string.punctuation     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```
- Pre-defined character sets for easy access
- No need to manually type all characters
- Standard across all Python installations

#### 2. **Random Module for Security**
```python
import random

# Select one random character
char = random.choice("abcdef")

# Shuffle list in-place
chars = ['a', 'b', 'c']
random.shuffle(chars)
```
- `random.choice()` picks one element randomly
- `random.shuffle()` randomizes list order
- Essential for unpredictable password generation

#### 3. **Generator Expressions with any()**
```python
# Check if ANY character meets condition
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in string.punctuation for c in password)
```
- `any()` returns True if at least one element is True
- Generator expressions are memory efficient
- Cleaner than writing loops manually

#### 4. **String Methods for Character Testing**
```python
char.isupper()  # Check if uppercase letter
char.islower()  # Check if lowercase letter
char.isdigit()  # Check if digit (0-9)
char.isalpha()  # Check if alphabetic character
```
- Built-in methods for character classification
- More reliable than manual checking
- Case-sensitive and locale-aware

#### 5. **List Manipulation**
```python
# Create empty list
password_chars = []

# Add single item
password_chars.append('A')

# Add multiple items
password_chars.extend(['B', 'C', 'D'])

# Shuffle in-place
random.shuffle(password_chars)

# Convert to string
password = ''.join(password_chars)
```
- Lists are mutable and easy to manipulate
- `extend()` adds multiple items at once
- `''.join()` converts list to string efficiently

#### 6. **Input Validation Pattern**
```python
while True:
    try:
        value = int(input("Enter number: "))
        if value >= minimum:
            return value
        else:
            print("Too small!")
    except ValueError:
        print("Not a number!")
```
- Loop until valid input received
- `try-except` catches conversion errors
- Provides helpful error messages

#### 7. **Dictionary for Structured Results**
```python
result = {
    'strength': 'Strong',
    'score': 5,
    'feedback': ['✓ All checks passed']
}

# Access values
print(result['strength'])  # 'Strong'
```
- Organize related data together
- Self-documenting with key names
- Easy to extend with new fields

### Key Takeaways

✅ **Guarantee security** - Don't rely on pure randomness for character types  
✅ **Validate everything** - User input needs try-except and range checks  
✅ **Visual feedback matters** - Emojis and bars improve user experience  
✅ **Modular functions** - Separate generation, validation, and display logic  
✅ **Security awareness** - Check common passwords, enforce minimum requirements

## Challenges & Solutions

### Challenge 1: Guaranteeing Character Types
**Problem**: Random generation might not include all selected character types

**Initial approach:**
```python
# Might generate "aaaaaaaa" (no digits/symbols!)
password = ''.join(random.choice(all_chars) for _ in range(length))
```

**Solution:**
```python
# Guarantee at least one of each type
password_chars = []
if use_upper:
    password_chars.append(random.choice(string.ascii_uppercase))
if use_digits:
    password_chars.append(random.choice(string.digits))

# Fill remaining with random
remaining = length - len(password_chars)
password_chars.extend(random.choice(all_chars) for _ in range(remaining))

# Shuffle to avoid predictable patterns
random.shuffle(password_chars)
```

### Challenge 2: Input Validation
**Problem**: Program crashes when user enters non-numeric input for length

**Solution:**
```python
def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length >= 8:
                return length
            else:
                print("❌ Password must be at least 8 characters!")
        except ValueError:
            print("❌ Please enter a valid number!")
```

### Challenge 3: Scoring System
**Problem**: How to weight different password criteria fairly

**Solution:**
```python
# Each criterion worth 1 point (max 5)
score = sum([
    len(password) >= 8,      # 1 point
    has_uppercase,            # 1 point
    has_lowercase,            # 1 point
    has_digit,               # 1 point
    has_special              # 1 point
])

# Override if common password
if is_common:
    strength = "Weak"
```

### Challenge 4: User Experience
**Problem**: Plain text output is boring and hard to scan

**Solution:**
```python
# Visual strength indicator
filled = "█" * score
empty = "░" * (5 - score)
print(f"[{filled}{empty}]")

# Emoji indicators
strength_emoji = {
    "Strong": "🟢",
    "Medium": "🟡",
    "Weak": "🔴"
}

# Check marks for passed/failed
symbol = "✓" if passed else "❌"
```

## Password Strength Criteria

### Scoring System
- ✅ **Length ≥ 8 characters** - 1 point
- ✅ **Has uppercase letters** - 1 point
- ✅ **Has lowercase letters** - 1 point
- ✅ **Has numbers** - 1 point
- ✅ **Has special characters** - 1 point

### Strength Levels
- **Strong (5/5)** 🟢 - All criteria met
- **Medium (3-4/5)** 🟡 - Most criteria met
- **Weak (0-2/5)** 🔴 - Few criteria met or common password

### Common Passwords Checked
```
password, 123456, 12345678, qwerty, abc123,
monkey, letmein, password1, 123123, welcome
```
(and more)

## Testing

### Test Cases
```
Generation:
✅ Test 1: Generate 8-character password - Passed
✅ Test 2: Generate 32-character password - Passed
✅ Test 3: Only uppercase selected - Works, includes uppercase
✅ Test 4: All options selected - Includes all types
✅ Test 5: No options selected - Shows error message
✅ Test 6: Invalid length (letters) - Handles error, asks again
✅ Test 7: Length < 8 - Sets to minimum 8

Validation:
✅ Test 8: "password" - Detected as weak/common
✅ Test 9: "Strong@Pass123" - Rated as strong
✅ Test 10: "weak" - Correctly identified as weak
✅ Test 11: "ALLUPPERCASE" - Missing lowercase/numbers/special
✅ Test 12: Empty password - Handled gracefully

Menu:
✅ Test 13: All menu options work
✅ Test 14: Invalid menu choice - Shows error
✅ Test 15: Exit option - Closes cleanly
✅ Test 16: Multiple operations - No memory issues
```

### Edge Cases Handled
- Minimum length enforcement (8 characters)
- No character types selected (error message)
- Non-numeric input for length (try-except)
- Empty password validation (feedback provided)
- Common password override (weak even if criteria met)

## Security Considerations

### What This Tool Does Well
✅ Generates truly random passwords  
✅ Ensures all selected character types are included  
✅ Checks against common passwords  
✅ Enforces minimum length requirements  
✅ Provides clear strength feedback

### Important Notes
⚠️ **This is an educational tool** - For production use, consider:
- Using `secrets` module instead of `random` for cryptographic strength
- Checking against larger breach databases (Have I Been Pwned API)
- Adding entropy calculation
- Implementing password history checking
- Using bcrypt/argon2 for storage (if storing passwords)

### Example Enhancement:
```python
import secrets  # More secure than random

# Instead of:
random.choice(characters)

# Use:
secrets.choice(characters)
```

## Future Improvements

### Version 2.0
- [ ] Use `secrets` module for cryptographic randomness
- [ ] Add password strength meter (entropy calculation)
- [ ] Save generated passwords to encrypted file
- [ ] Password history (avoid repeats)
- [ ] Pronounceable password option

### Version 3.0
- [ ] Check against Have I Been Pwned API
- [ ] Generate passphrases (diceware method)
- [ ] Multiple passwords at once
- [ ] Export to CSV/JSON
- [ ] Memorable password patterns

### Version 4.0
- [ ] GUI with Tkinter
- [ ] Browser extension
- [ ] Password manager integration
- [ ] QR code generation
- [ ] Two-factor authentication codes

## Project Statistics

| Metric | Value |
|--------|-------|
| **Lines of Code** | ~220 |
| **Functions** | 9 |
| **Time to Complete** | ~3 hours |
| **Difficulty** | ⭐⭐ Intermediate |
| **Date Completed** | January 2026 |

### Time Breakdown
- Understanding requirements: 15 minutes
- Initial implementation: 45 minutes
- Adding guaranteed character types: 30 minutes
- Input validation: 30 minutes
- Menu system: 25 minutes
- Validation display formatting: 30 minutes
- Testing and debugging: 30 minutes
- Documentation: 25 minutes

## Comparison with Previous Projects

| Aspect | Project 04 | Project 05 |
|--------|------------|------------|
| **Main Data Structure** | Lists | Strings + Dicts |
| **User Input** | Numbers + operators | Text + booleans |
| **Randomness** | None | Core feature |
| **Validation** | Math operations | String analysis |
| **Output** | Calculations | Generated passwords |
| **Security Focus** | None | High |

### Evolution from Project 04
- **String manipulation mastery** - Learned character checking methods
- **Security awareness** - Understanding password best practices
- **Random module** - Generating unpredictable values
- **Visual design** - Using emojis and symbols effectively
- **Error prevention** - Guaranteeing output quality

## Common Use Cases

**1. Creating Strong Passwords:**
```
Use Case: New account signup
Action: Generate → 16 chars, all types
Result: K9$mPq2X@5TnLv
```

**2. Checking Existing Passwords:**
```
Use Case: Audit current passwords
Action: Validate → Enter "password123"
Result: Weak (common password detected)
```

**3. Quick Strong Password:**
```
Use Case: Need password now
Action: Generate & Validate → Shows strength immediately
Result: Strong password with confidence
```

## Useful Commands

```bash
# Run the tool
python password_tool.py

# Run with Python 3 specifically
python3 password_tool.py

# Check Python version
python --version
```

## Dependencies

**Standard Library Only:**
- `random` - Random number generation
- `string` - String constants and operations

**No external packages required!** ✨

## Reflection

### What I'm Proud Of
- Guaranteeing character types in generation (more secure than pure random)
- Clean separation of generation and validation logic
- Visual feedback with emojis and progress bars
- Comprehensive input validation (program never crashes)
- Common password detection (real security consideration)

### What I Struggled With
- Ensuring generated passwords always include selected types
- Deciding on the scoring system for password strength
- Making the validation output easy to read and actionable
- Balancing security with usability
- Testing all edge cases thoroughly

### How I Improved from Project 04
- **Better randomness** - Used random module effectively
- **Security mindset** - Thought about real-world password concerns
- **String mastery** - Comfortable with all string operations
- **Input validation** - More robust error handling
- **User feedback** - Visual indicators improve experience

### Key Lessons Learned
1. **Security is hard** - Even simple password generation has many considerations
2. **Guarantees matter** - Don't rely on probability for critical requirements
3. **Feedback quality** - Good error messages prevent user frustration
4. **Test edge cases** - Empty inputs, invalid types, boundary values
5. **Visual design** - Small touches (emojis, bars) make big difference

## Links

- **Code**: [`password_tool.py`](./password_tool.py)

## Resources Used

- [Python random module](https://docs.python.org/3/library/random.html)
- [Python string module](https://docs.python.org/3/library/string.html)
- [OWASP Password Guidelines](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- Common passwords list research

---

**Part of:** [30 Python Mini Projects](https://github.com/engineerliyong/python-mini-projects)  
**Author:** [Liza Bambu](https://github.com/engineerliyong)  
**Date:** February 2026  
**Status:** ✅ Complete  
**Next:** Project 06 - JSON Contact Manager

---

## Contributing

Found a bug or have a suggestion? Open an issue in the [main repository](https://github.com/engineerliyong/python-mini-projects/issues) and tag it with `project-05`.

---

*Building Python skills one project at a time* 🚀