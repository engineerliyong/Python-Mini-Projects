"""
Contact Manager
Author: Liza Bambu
Date: April 2026

Manage contacts with JSON storage - Add, view, search, update, and delete.
"""

import json
import os
import re

FILE_NAME = "contacts.json"


# Load contacts from file
def load_contacts():
    """Load contacts from JSON file"""
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            # Handle both old format (list) and new format (dict with contacts key)
            if isinstance(data, list):
                return data
            return data.get("contacts", [])
    except json.JSONDecodeError:
        print("⚠️  Warning: Corrupted file. Starting fresh.")
        return []


# Save contacts to file
def save_contacts(contacts):
    """Save contacts to JSON file"""
    try:
        with open(FILE_NAME, "w") as file:
            data = {"contacts": contacts}
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"❌ Error saving: {e}")
        return False


def get_next_id(contacts):
    """Get next available ID"""
    if not contacts:
        return 1
    return max(contact.get('id', 0) for contact in contacts) + 1


def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_phone(phone):
    """Validate phone number (at least 10 digits)"""
    digits = re.sub(r'[^\d]', '', phone)
    return len(digits) >= 10


# Add contact
def add_contact():
    """Add new contact with validation"""
    contacts = load_contacts()
    
    print("\n" + "-" * 60)
    print("  ADD NEW CONTACT")
    print("-" * 60)
    
    # Get and validate name
    name = input("\nEnter name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    # Get and validate phone
    while True:
        phone = input("Enter phone: ").strip()
        if not phone:
            print("❌ Phone cannot be empty!")
            continue
        if validate_phone(phone):
            break
        else:
            print("❌ Phone must have at least 10 digits!")
    
    # Get and validate email
    while True:
        email = input("Enter email: ").strip()
        if not email:
            print("❌ Email cannot be empty!")
            continue
        if validate_email(email):
            break
        else:
            print("❌ Invalid email format!")
    
    # Create contact with ID
    contact = {
        "id": get_next_id(contacts),
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts.append(contact)
    
    if save_contacts(contacts):
        print(f"\n✅ Contact added successfully! (ID: {contact['id']})")
    else:
        print("\n❌ Failed to save contact!")


# View contacts
def view_contacts():
    """Display all contacts in a formatted table"""
    contacts = load_contacts()
    
    if not contacts:
        print("\n📭 No contacts found.")
        return
    
    print("\n" + "=" * 80)
    print("  ALL CONTACTS")
    print("=" * 80)
    print(f"{'ID':<5} {'Name':<25} {'Phone':<20} {'Email':<30}")
    print("-" * 80)
    
    for contact in contacts:
        contact_id = contact.get('id', '?')
        print(f"{contact_id:<5} {contact['name']:<25} {contact['phone']:<20} {contact['email']:<30}")
    
    print("-" * 80)
    print(f"Total: {len(contacts)} contact(s)")
    print("=" * 80)


# Search contact
def search_contact():
    """Search contacts by name"""
    contacts = load_contacts()
    
    if not contacts:
        print("\n📭 No contacts to search!")
        return
    
    print("\n" + "-" * 60)
    print("  SEARCH CONTACTS")
    print("-" * 60)
    
    keyword = input("\nEnter name to search: ").strip().lower()
    
    if not keyword:
        print("❌ Search term cannot be empty!")
        return
    
    found = []
    for contact in contacts:
        if keyword in contact["name"].lower():
            found.append(contact)
    
    if not found:
        print(f"\n❌ No contacts found matching '{keyword}'")
        return
    
    print(f"\n✓ Found {len(found)} contact(s):")
    print("-" * 80)
    print(f"{'ID':<5} {'Name':<25} {'Phone':<20} {'Email':<30}")
    print("-" * 80)
    
    for contact in found:
        contact_id = contact.get('id', '?')
        print(f"{contact_id:<5} {contact['name']:<25} {contact['phone']:<20} {contact['email']:<30}")
    
    print("-" * 80)


def find_contact_by_id(contacts, contact_id):
    """Find contact by ID"""
    for contact in contacts:
        if contact.get('id') == contact_id:
            return contact
    return None


# Update contact
def update_contact():
    """Update existing contact by ID"""
    contacts = load_contacts()
    
    if not contacts:
        print("\n📭 No contacts to update!")
        return
    
    print("\n" + "-" * 60)
    print("  UPDATE CONTACT")
    print("-" * 60)
    
    # Show all contacts first
    view_contacts()
    
    # Get ID to update
    try:
        contact_id = int(input("\nEnter contact ID to update: ").strip())
    except ValueError:
        print("❌ Invalid ID!")
        return
    
    # Find contact
    contact = find_contact_by_id(contacts, contact_id)
    
    if not contact:
        print(f"❌ Contact with ID {contact_id} not found!")
        return
    
    # Show current contact
    print(f"\nCurrent contact:")
    print(f"  Name: {contact['name']}")
    print(f"  Phone: {contact['phone']}")
    print(f"  Email: {contact['email']}")
    
    print("\nLeave blank to keep current value.")
    
    # Get new name
    new_name = input(f"New name [{contact['name']}]: ").strip()
    if new_name:
        contact["name"] = new_name
    
    # Get new phone with validation
    while True:
        new_phone = input(f"New phone [{contact['phone']}]: ").strip()
        if not new_phone:
            break
        if validate_phone(new_phone):
            contact["phone"] = new_phone
            break
        else:
            print("❌ Invalid phone number!")
    
    # Get new email with validation
    while True:
        new_email = input(f"New email [{contact['email']}]: ").strip()
        if not new_email:
            break
        if validate_email(new_email):
            contact["email"] = new_email
            break
        else:
            print("❌ Invalid email format!")
    
    if save_contacts(contacts):
        print("\n✅ Contact updated!")
    else:
        print("\n❌ Failed to save changes!")


# Delete contact
def delete_contact():
    """Delete contact by ID with confirmation"""
    contacts = load_contacts()
    
    if not contacts:
        print("\n📭 No contacts to delete!")
        return
    
    print("\n" + "-" * 60)
    print("  DELETE CONTACT")
    print("-" * 60)
    
    # Show all contacts first
    view_contacts()
    
    # Get ID to delete
    try:
        contact_id = int(input("\nEnter contact ID to delete: ").strip())
    except ValueError:
        print("❌ Invalid ID!")
        return
    
    # Find contact
    contact = find_contact_by_id(contacts, contact_id)
    
    if not contact:
        print(f"❌ Contact with ID {contact_id} not found!")
        return
    
    # Show contact to be deleted
    print(f"\nContact to delete:")
    print(f"  ID: {contact['id']}")
    print(f"  Name: {contact['name']}")
    print(f"  Phone: {contact['phone']}")
    print(f"  Email: {contact['email']}")
    
    # Confirm deletion
    confirm = input("\nAre you sure you want to delete this contact? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        contacts.remove(contact)
        
        if save_contacts(contacts):
            print("\n🗑️  Contact deleted successfully!")
        else:
            print("\n❌ Failed to save changes!")
    else:
        print("\n✗ Deletion cancelled.")


# Menu
def menu():
    """Main menu loop"""
    print("\n" + "=" * 60)
    print("  WELCOME TO CONTACT MANAGER")
    print("=" * 60)
    
    contacts = load_contacts()
    print(f"✓ Loaded {len(contacts)} contact(s)")
    
    while True:
        print("\n" + "=" * 60)
        print("  CONTACT MANAGER")
        print("=" * 60)
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("=" * 60)
        
        choice = input("\nChoose an option (1-6): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            contacts = load_contacts()
            print("\n" + "=" * 60)
            print("  Thank you for using Contact Manager!")
            print("=" * 60)
            print(f"  Total contacts saved: {len(contacts)}")
            print("=" * 60)
            print("\nGoodbye! 📇\n")
            break
        else:
            print("\n❌ Invalid choice. Please enter 1-6.")


# Run program
if __name__ == "__main__":
    menu()