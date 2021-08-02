import os

ADD_CHOICE = 1
SHOW_CHOICE = 2
SEARCH_CHOICE = 3
MODIFY_CHOICE = 4
DELETE_CHOICE = 5
QUIT_CHOICE = 6

def main():
    choice = 0
    try:
        while choice != QUIT_CHOICE:
            display_menu()

            choice = int(input('Enter your choice: '))

            if choice == ADD_CHOICE:
                add()
            elif choice == SHOW_CHOICE:
                show()
            elif choice == SEARCH_CHOICE:
                search()
            elif choice == MODIFY_CHOICE:
                modify()
            elif choice == DELETE_CHOICE:
                delete()
            elif choice == QUIT_CHOICE:
                print('Exiting the program...')
            else:
                print('Error: invalid selection.')

    except :
        print("Error: Wrong Datatype - Try again with integer value!!! \n")

    
def display_menu():
    print('  CHOICE MENU  ')
    print('1) Add a contact')
    print('2) Show the list of contacts')
    print('3) Search for a name in the list')
    print('4) Modify a contact')
    print('5) Delete a contact form the list')    
    print('6) Quit')
    
def add():
    another = 'y'

    contact_file = open('contact.txt', 'a')

    while another == 'y' or another == 'Y':
        print('Enter the following contact info:')
        name = input('Name: ')
        email = str(input('Email: '))
        phone = str(input('Phone: '))

        contact_file.write(name + '\n')
        contact_file.write(email + '\n')
        contact_file.write(phone + '\n')

        print('Do you want to add another record?')
        another = input('Y = yes, anything else = no: ')

    contact_file.close()
    print('Data appended to contact.txt.')
    
def show():
    
    try:
        contact_file = open('contact.txt', 'r')

        name = contact_file.readline()
        print('\nList of contact(s): ')
        i = 1
        # Read the rest of the file.
        while name != '':
            
            email = str(contact_file.readline())
            phone = str(contact_file.readline())

            # Strip the \n from name.
            name = name.rstrip('\n')
            email =email.rstrip('\n')
            phone = phone.rstrip('\n')
            # Display the record.
            print("Contact #",i)
            print('\t\tName:', name)
            print('\t\tEmail:', email)
            print('\t\tPhone:', phone)
            print("-------------------------------------")
            

            # Read the next description.
            name = contact_file.readline()
            i = i + 1
        # Close the file.
        contact_file.close()
        
    except IOError as err:
        print(err)
    
def search():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value.
    search = input('Enter a name to search: ')

    # Open the contact.txt file.
    contact_file = open('contact.txt', 'r')

    # Read the first record's description field.
    name = contact_file.readline()

    # Read the rest of the file.
    while name != '':
        email = str(contact_file.readline())
        phone = str(contact_file.readline())

        # Strip the \n from the name.
        name = name.rstrip('\n')
        email =email.rstrip('\n')
        phone = phone.rstrip('\n')


        # Determine whether this record matches
        # the search value.
        if name == search:
            # Display the record.
            print('Name:', name)
            print('Email:', email)
            print('Phone:', phone)
            print()
            # Set the found flag to True.
            found = True

        # Read the next description.
        name = contact_file.readline()

    # Close the file.
    contact_file.close()

    # If the search value was not found in the file
    # display a message.
    if not found:
        print('That item was not found in the file.')

def modify():
    
    # Create a bool variable to use as a flag.
    found = False

    search = input('Enter a name to search for update: ')
    new_email = str(input('Enter the new email for update: '))
    new_phone = str(input('Enter the new phone for update: '))
    
    # Open the original contact.txt file.
    contact_file = open('contact.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    name = contact_file.readline()

    # Read the rest of the file.
    while name != '':
        email = str(contact_file.readline())
        phone = str(contact_file.readline())
        name = name.rstrip('\n')
        email =email.rstrip('\n')
        phone = phone.rstrip('\n')

        if name == search:
            # Write the modified record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(new_email + '\n')
            temp_file.write(new_phone + '\n')
            
            # Set the found flag to True.
            found = True
        else:
            # Write the original record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(email + '\n')
            temp_file.write(phone + '\n')

        name = contact_file.readline()

    # Close the contact file and the temporary file.
    contact_file.close()
    temp_file.close()

    # Delete the original contact.txt file.
    os.remove('contact.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'contact.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')
        
def delete():
    # Create a bool variable to use as a flag.
    found = False

    # Get the name to delete.
    search = input('Which name do you want to delete? ')
    
    # Open the original contact.txt file.
    contact_file = open('contact.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first record's name field.
    name = contact_file.readline()

    # Read the rest of the file.
    while name != '':
        email = str(contact_file.readline())

        phone = str(contact_file.readline())

        # Strip the \n from name.
        name = name.rstrip('\n')
        email =email.rstrip('\n')
        phone = phone.rstrip('\n')

        # If this is not the record to delete, then
        # write it to the temporary file.
        if name != search:
            # Write the record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(email + '\n')
            temp_file.write(phone + '\n')
        else:
            # Set the found flag to True.
            found = True

        # Read the next name.
        name = contact_file.readline()

    # Close the contact file and the temporary file.
    contact_file.close()
    temp_file.close()

    # Delete the original contact.txt file.
    os.remove('contact.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'contact.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')
        

main()