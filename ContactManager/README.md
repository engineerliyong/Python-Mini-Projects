# Contact Manager 📇

**Project 06** of 30 Python Mini Projects

A JSON-based contact management system with full CRUD operations, input validation, and data persistence.

## Features

- ✅ **Add Contacts** - Store name, phone, and email with validation
- ✅ **View All Contacts** - Display contacts in formatted table
- ✅ **Search Contacts** - Find contacts by name
- ✅ **Update Contacts** - Edit existing contact information
- ✅ **Delete Contacts** - Remove contacts with confirmation
- ✅ **Unique IDs** - Each contact has a unique identifier
- ✅ **Input Validation** - Email and phone format checking
- ✅ **Data Persistence** - Auto-save to JSON file
- ✅ **Error Handling** - Graceful handling of corrupted files

## Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies (uses standard library only)

### Setup
```bash
# Clone the repository
git clone https://github.com/engineerliyong/python-mini-projects.git

# Navigate to this project
cd python-mini-projects/project-06-contact-manager

# Run the program
python contact_manager.py
```

## Usage

### Starting the Program
```bash
python contact_manager.py
```

### Example Session

**Adding a Contact:**
```
============================================================
  CONTACT MANAGER
============================================================
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
============================================================

Choose an option (1-6): 1

------------------------------------------------------------
  ADD NEW CONTACT
------------------------------------------------------------

Enter name: Alice Johnson
Enter phone: +1234567890
Enter email: alice@example.com

✅ Contact added successfully! (ID: 1)
```

**Viewing Contacts:**
```
Choose an option (1-6): 2

================================================================================
  ALL CONTACTS
================================================================================
ID    Name                      Phone                Email
--------------------------------------------------------------------------------
1     Alice Johnson             +1234567890          alice@example.com
2     Bob Smith                 +9876543210          bob@example.com
--------------------------------------------------------------------------------
Total: 2 contact(s)
================================================================================
```

**Searching Contacts:**
```
Choose an option (1-6): 3

------------------------------------------------------------
  SEARCH CONTACTS
------------------------------------------------------------

Enter name to search: alice

✓ Found 1 contact(s):
--------------------------------------------------------------------------------
ID    Name                      Phone                Email
--------------------------------------------------------------------------------
1     Alice Johnson             +1234567890          alice@example.com
--------------------------------------------------------------------------------
```

**Updating a Contact:**
```
Choose an option (1-6): 4

Enter contact ID to update: 1

Current contact:
  Name: Alice Johnson
  Phone: +1234567890
  Email: alice@example.com

Leave blank to keep current value.
New name [Alice Johnson]: 
New phone [+1234567890]: +1234567899
New email [alice@example.com]: alice.j@example.com

✅ Contact updated!
```

**Deleting a Contact:**
```
Choose an option (1-6): 5

Enter contact ID to delete: 1

Contact to delete:
  ID: 1
  Name: Alice Johnson
  Phone: +1234567899
  Email: alice.j@example.com

Are you sure you want to delete this contact? (yes/no): yes

🗑️  Contact deleted successfully!
```

## Code Structure

### Main Functions

**File Operations:**
```python
load_contacts()        # Load contacts from JSON file
save_contacts(contacts)  # Save contacts to JSON file
```

**Helper Functions:**
```python
get_next_id(contacts)           # Generate unique ID
validate_email(email)            # Validate email format
validate_phone(phone)            # Validate phone number
find_contact_by_id(contacts, id) # Find contact by ID
```

**CRUD Operations:**
```python
add_contact()      # Create new contact
view_contacts()    # Read/display all contacts
search_contact()   # Read/search specific contacts
update_contact()   # Update existing contact
delete_contact()   # Delete contact
```

**Program Flow:**
```python
menu()  # Main loop with menu system
```

### Data Structure

**JSON File Format:**
```json
{
  "contacts": [
    {
      "id": 1,
      "name": "Alice Johnson",
      "phone": "+1234567890",
      "email": "alice@example.com"
    },
    {
      "id": 2,
      "name": "Bob Smith",
      "phone": "+9876543210",
      "email": "bob@example.com"
    }
  ]
}
```

**In-Memory Format:**
```python
contacts = [
    {"id": 1, "name": "Alice", "phone": "...", "email": "..."},
    {"id": 2, "name": "Bob", "phone": "...", "email": "..."}
]
```

## What I Learned

### Python Concepts

#### 1. **JSON Module**
```python
import json

# Reading JSON
with open('file.json', 'r') as file:
    data = json.load(file)

# Writing JSON
with open('file.json', 'w') as file:
    json.dump(data, file, indent=4)
```
- `json.load()` parses JSON from file to Python objects
- `json.dump()` writes Python objects to file as JSON
- `indent=4` makes JSON human-readable

#### 2. **File Operations with os Module**
```python
import os

# Check if file exists
if os.path.exists(filename):
    # File exists
else:
    # File doesn't exist
```
- `os.path.exists()` checks file existence
- Prevents errors when loading files
- Returns True/False

#### 3. **Regular Expressions for Validation**
```python
import re

# Email validation
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
is_valid = re.match(pattern, email) is not None

# Extract only digits
digits = re.sub(r'[^\d]', '', phone)
```
- `re.match()` checks if string matches pattern
- `re.sub()` replaces matched patterns
- Regex patterns define validation rules

#### 4. **Dictionary get() Method**
```python
# Safe dictionary access
contact_id = contact.get('id', 0)  # Returns 0 if 'id' key doesn't exist

# vs
contact_id = contact['id']  # Raises KeyError if 'id' doesn't exist
```
- `.get(key, default)` returns default if key missing
- Prevents KeyError exceptions
- Useful for backward compatibility

#### 5. **List Filtering**
```python
# Find matching contacts
found = [c for c in contacts if keyword in c["name"].lower()]

# Remove contact
contacts.remove(contact)  # Removes first matching item
```
- List comprehension for filtering
- `.remove()` deletes item from list
- Case-insensitive search with `.lower()`

#### 6. **Try-Except for Error Handling**
```python
try:
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
except json.JSONDecodeError:
    print("Corrupted file")
    return []
except FileNotFoundError:
    return []
```
- Multiple except clauses for different errors
- Specific exception handling
- Graceful degradation

#### 7. **Input Validation Loops**
```python
while True:
    email = input("Enter email: ").strip()
    if validate_email(email):
        break  # Valid, exit loop
    else:
        print("Invalid format!")
        # Loop continues
```
- Loop until valid input
- `.strip()` removes whitespace
- Break when validation passes

### Key Takeaways

✅ **JSON is perfect for simple data storage** - Easy to read and edit  
✅ **Unique IDs prevent confusion** - Can have duplicate names safely  
✅ **Validation prevents bad data** - Check before storing  
✅ **Confirmation prevents accidents** - Ask before deleting  
✅ **Formatted output improves UX** - Tables are easier to scan than plain text

## Challenges & Solutions

### Challenge 1: Handling Duplicate Names
**Problem**: Multiple contacts with same name

**Initial approach:**
```python
# Search/update/delete by name
for contact in contacts:
    if contact["name"] == name:
        # Only finds FIRST match!
```

**Solution**: Add unique ID system
```python
def get_next_id(contacts):
    if not contacts:
        return 1
    return max(contact.get('id', 0) for contact in contacts) + 1

# Update/delete by ID instead of name
```

### Challenge 2: Validating Email and Phone
**Problem**: Accepting invalid formats

**Solution**: Regular expressions
```python
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    digits = re.sub(r'[^\d]', '', phone)
    return len(digits) >= 10
```

### Challenge 3: File Doesn't Exist on First Run
**Problem**: Program crashes when JSON file missing

**Solution**: Check file existence
```python
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []  # Return empty list
    # Otherwise load file
```

### Challenge 4: Corrupted JSON File
**Problem**: Manual edits can break JSON format

**Solution**: Handle JSON decode errors
```python
try:
    data = json.load(file)
except json.JSONDecodeError:
    print("Warning: Corrupted file")
    return []
```

### Challenge 5: Accidental Deletions
**Problem**: Easy to delete wrong contact

**Solution**: Show contact and confirm
```python
# Show what will be deleted
print(f"Contact to delete:")
print(f"  Name: {contact['name']}")

# Require explicit confirmation
confirm = input("Are you sure? (yes/no): ")
if confirm == 'yes':
    # Delete
```

## Input Validation Rules

### Email Validation
- Must contain `@` symbol
- Must contain `.` after @
- Must follow pattern: `name@domain.extension`
- Examples:
  - ✅ `alice@example.com`
  - ✅ `bob.smith@company.co.uk`
  - ❌ `invalidemail`
  - ❌ `missing@domain`

### Phone Validation
- Must contain at least 10 digits
- Ignores spaces, dashes, parentheses
- Examples:
  - ✅ `+1234567890`
  - ✅ `(123) 456-7890`
  - ✅ `123 456 7890`
  - ❌ `123456` (too short)

### Name Validation
- Cannot be empty
- Whitespace trimmed
- Examples:
  - ✅ `Alice Johnson`
  - ✅ `Bob`
  - ❌ `` (empty)
  - ❌ `   ` (only spaces)

## Testing

### Test Cases
```
File Operations:
✅ Test 1: First run (no file) - Creates empty list
✅ Test 2: Load existing file - Loads contacts
✅ Test 3: Corrupted JSON - Handles gracefully
✅ Test 4: Save after add - File updated

CRUD Operations:
✅ Test 5: Add contact - Contact appears in list
✅ Test 6: Add with invalid email - Rejected
✅ Test 7: Add with invalid phone - Rejected
✅ Test 8: View empty list - Shows "No contacts"
✅ Test 9: View with contacts - Shows formatted table
✅ Test 10: Search found - Displays matches
✅ Test 11: Search not found - Shows message
✅ Test 12: Update by ID - Changes saved
✅ Test 13: Update blank fields - Keeps original
✅ Test 14: Delete with confirm - Contact removed
✅ Test 15: Delete cancelled - Contact kept

Edge Cases:
✅ Test 16: Duplicate names - IDs distinguish them
✅ Test 17: Invalid ID for update - Error message
✅ Test 18: Invalid ID for delete - Error message
✅ Test 19: Exit - Shows total count
```

### Manual Testing Checklist
```
□ Add 3 contacts successfully
□ View all contacts in table
□ Search for existing contact
□ Search for non-existent contact
□ Update contact phone
□ Update contact with blank (keeps original)
□ Try to add contact with invalid email
□ Try to add contact with invalid phone
□ Delete contact after confirmation
□ Cancel deletion
□ Exit and restart - contacts persist
```

## File Structure

```
project-06-contact-manager/
├── contact_manager.py    # Main program
├── contacts.json         # Data file (auto-created)
└── README.md            # This file
```

## Future Improvements

### Version 2.0
- [ ] Import contacts from CSV
- [ ] Export contacts to CSV
- [ ] Add contact categories/groups
- [ ] Add birthday field
- [ ] Birthday reminders

### Version 3.0
- [ ] Multiple phone numbers per contact
- [ ] Add address field
- [ ] Add notes field
- [ ] Profile pictures
- [ ] Backup/restore functionality

### Version 4.0
- [ ] GUI with Tkinter
- [ ] SQLite database instead of JSON
- [ ] Contact sync with cloud
- [ ] vCard import/export
- [ ] Integration with email clients

## Project Statistics

| Metric | Value |
|--------|-------|
| **Lines of Code** | ~280 |
| **Functions** | 11 |
| **Time to Complete** | ~3.5 hours |
| **Difficulty** | ⭐⭐ Intermediate |
| **Date Completed** | January 2026 |

### Time Breakdown
- Understanding JSON: 20 minutes
- Basic CRUD implementation: 60 minutes
- Adding ID system: 30 minutes
- Input validation: 40 minutes
- Error handling: 25 minutes
- Formatting/UI improvements: 30 minutes
- Testing: 30 minutes
- Documentation: 25 minutes

## Comparison with Previous Projects

| Aspect | Project 05 | Project 06 |
|--------|------------|------------|
| **Data Storage** | None | JSON file |
| **Data Structure** | Strings | Dictionaries in list |
| **Validation** | Email/phone patterns | Email/phone + IDs |
| **Operations** | Generate/validate | Full CRUD |
| **Persistence** | No | Yes (file-based) |
| **IDs** | No | Yes (unique IDs) |

### Evolution from Project 05
- **Data persistence** - First project with file storage
- **CRUD mastery** - Complete Create, Read, Update, Delete
- **ID system** - Managing unique identifiers
- **JSON proficiency** - Reading/writing structured data
- **Better validation** - Regex for complex patterns

## Common Issues & Solutions

**Issue**: "File not found" error
- **Solution**: Program creates file automatically on first run

**Issue**: Corrupted JSON file
- **Solution**: Delete `contacts.json` and restart program

**Issue**: Can't update/delete contact
- **Solution**: Use the ID number, not the name

**Issue**: Email/phone validation too strict
- **Solution**: Modify regex patterns in `validate_email()` and `validate_phone()`

## Useful Commands

```bash
# Run the program
python contact_manager.py

# View JSON file (pretty print)
python -m json.tool contacts.json

# Backup contacts
cp contacts.json contacts_backup.json

# Reset (delete all contacts)
rm contacts.json
```

## Dependencies

**Standard Library Only:**
- `json` - JSON encoding/decoding
- `os` - File system operations
- `re` - Regular expressions

**No external packages required!** ✨

## Reflection

### What I'm Proud Of
- Clean JSON structure that's easy to edit manually
- Unique ID system prevents duplicate name confusion
- Comprehensive input validation (email, phone, empty fields)
- Formatted table output is easy to read
- Delete confirmation prevents accidents
- Backward compatible (handles contacts without IDs)

### What I Struggled With
- Understanding regex patterns for email validation
- Deciding between update by name vs. ID
- Handling backward compatibility with old JSON format
- Making table formatting work with different name lengths
- Testing all edge cases thoroughly

### How I Improved from Project 05
- **Data persistence** - First project storing data permanently
- **CRUD operations** - Complete lifecycle management
- **Structured data** - Working with nested dictionaries
- **File handling** - Reading/writing JSON files
- **ID management** - Generating and tracking unique identifiers

### Key Lessons Learned
1. **Unique IDs are essential** - Names aren't reliable identifiers
2. **JSON is great for simple storage** - Easy to read, edit, and parse
3. **Validate early** - Reject bad data at input, not later
4. **Confirm destructive actions** - Ask before deleting
5. **Handle file errors** - Files can be missing, corrupted, or locked
6. **Regex is powerful** - Perfect for pattern matching

## Links

- **Code**: [`contact_manager.py`](./contact_manager.py)
- **Sample Data**: [`contacts.json`](./contacts.json)

## Resources Used

- [Python JSON module](https://docs.python.org/3/library/json.html)
- [Python os module](https://docs.python.org/3/library/os.html)
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Email regex patterns](https://emailregex.com/)

---

**Part of:** [30 Python Mini Projects](https://github.com/engineerliyong/python-mini-projects)  
**Author:** [Liza Bambu](https://github.com/engineerliyong)  
**Date:** April 2026  
**Status:** ✅ Complete  
**Next:** Project 07 - Directory File Organizer

---

## Contributing

Found a bug or have a suggestion? Open an issue in the [main repository](https://github.com/engineerliyong/python-mini-projects/issues) and tag it with `project-06`.

---

*Building Python skills one project at a time* 🚀