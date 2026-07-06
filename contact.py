#empty dictionary
contacts = {}

while True:
    print('\nContact Book App')
    print('1. Add Contact')
    print('2. View Contacts')   
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contacts')
    print('7. Exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        name = input('Enter Name :')
        if name in contacts:
            print('Contact already exists.')
        else:
            email = input('Enter Email :')
            mobile = int(input('Enter Mobile number:'))
            contacts[name] = {"email" : email, "mobile" : mobile}
            print(f'Contact {name} added successfully.')
    
    
    elif choice == 2:
        name = input('Enter Name to view contact:')
        if name in contacts:
            contact = contacts[name]
            print(contact["email"], contact["mobile"])
        else:
            print('Contact not found.')
   
   
    elif choice == 3:
        name = input('Enter Name to update contact:')
        if name in contacts:
            email = input('Enter new Email :')
            mobile = int(input('Enter new Mobile number:'))
            contacts[name] = {"email": email, "mobile": mobile}
            print(f'Contact {name} updated successfully.')
        else:
            print('Contact not found.')
        
    elif choice == 4:
        name = input('Enter Name to delete contact:')
        if name in contacts:
            del contacts[name]
            print(f'Contact {name} deleted successfully.')
        else:
            print('Contact not found.')

    elif choice == 5:
        search_name = input('Enter Name to search contact:')
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Name: {name}, Email: {contact["email"]}, Mobile Number: {contact["mobile"]}')
                found = True
        if not found:
            print('Contact not found.')

    
    elif choice == 6:
        print(f'Total contacts: {len(contacts)}')

    
    elif choice == 7:
        print('Exiting the program.')
        break

    else:
        print('Invalid choice. Please try again.')
