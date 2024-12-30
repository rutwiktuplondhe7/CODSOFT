def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact {name} added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    for name, details in contacts.items():
        if search_term in name or search_term in details['phone']:
            print(f"Found contact - Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            return
    print("Contact not found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
