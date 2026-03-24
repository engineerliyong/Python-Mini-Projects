import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add contact
def add_contact():
    contacts = load_contacts()
    
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("✅ Contact added successfully!")

# View contacts
def view_contacts():
    contacts = load_contacts()
    
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")

# Search contact
def search_contact():
    contacts = load_contacts()
    keyword = input("Enter name to search: ").lower()

    found = False
    for contact in contacts:
        if keyword in contact["name"].lower():
            print("\nFound Contact:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True

    if not found:
        print("❌ Contact not found.")

# Update contact
def update_contact():
    contacts = load_contacts()
    name = input("Enter name to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("Leave blank to keep current value.")
            
            new_phone = input(f"New phone ({contact['phone']}): ")
            new_email = input(f"New email ({contact['email']}): ")

            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email

            save_contacts(contacts)
            print("✅ Contact updated!")
            return

    print("❌ Contact not found.")

# Delete contact
def delete_contact():
    contacts = load_contacts()
    name = input("Enter name to delete: ").lower()

    new_contacts = [c for c in contacts if c["name"].lower() != name]

    if len(new_contacts) == len(contacts):
        print("❌ Contact not found.")
    else:
        save_contacts(new_contacts)
        print("🗑️ Contact deleted.")

# Menu
def menu():
    while True:
        print("\n==== Contact Manager ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run program
if __name__ == "__main__":
    menu()