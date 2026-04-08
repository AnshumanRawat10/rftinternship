# Phonebook dictionary
phonebook = {
    "AMIT": "9876543210",
    "RIYA": "9123456780"
}

# Add contact
def add_contact(name, number):
    name = name.upper()
    
    if name in phonebook:
        print("Contact already exists!")
    else:
        phonebook[name] = number
        print("Contact added successfully!")

# Search contact (with partial search)
def search_contact(name):
    name = name.upper()
    found = False
    
    for contact in phonebook:
        if name in contact:   # partial search
            print(f"{contact} : {phonebook[contact]}")
            found = True
    
    if not found:
        print("Contact not found!")

# Delete contact
def delete_contact(name):
    name = name.upper()
    
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted!")
    else:
        print("Contact not found!")

# Display all contacts
def show_all():
    print("\nPhonebook:")
    for name, number in phonebook.items():
        print(f"{name} : {number}")

# Menu-driven program
while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
        
    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)
        
    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)
        
    elif choice == "4":
        show_all()
        
    elif choice == "5":
        print("Exiting...")
        break
        
    else:
        print("Invalid choice!")