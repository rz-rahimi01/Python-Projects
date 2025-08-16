import json
import os

FILE_NAME = "contacts.json"

# Load contacts
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Save contacts
def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(name, phone, email):
    contacts = load_contacts()
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print(f"✅ Contact added: {name}")

# List all contacts
def list_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n===== CONTACTS =====")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']} - {c['email']}")

# Search contacts
def search_contacts(keyword):
    contacts = load_contacts()
    results = [c for c in contacts if keyword.lower() in c["name"].lower()]
    if not results:
        print("❌ No contacts found.")
        return
    print("\n===== SEARCH RESULTS =====")
    for i, c in enumerate(results, start=1):
        print(f"{i}. {c['name']} - {c['phone']} - {c['email']}")

# Delete a contact
def delete_contact(index):
    contacts = load_contacts()
    if 0 <= index < len(contacts):
        removed = contacts.pop(index)
        save_contacts(contacts)
        print(f"🗑 Contact deleted: {removed['name']}")
    else:
        print("❌ Invalid index.")

# Main menu
def main():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            add_contact(name, phone, email)
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            keyword = input("Enter name to search: ").strip()
            search_contacts(keyword)
        elif choice == "4":
            list_contacts()
            try:
                idx = int(input("Enter contact number to delete: ")) - 1
                delete_contact(idx)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
