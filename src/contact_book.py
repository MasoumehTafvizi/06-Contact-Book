class ContactBook:
    """
    A class used to represent a Contact Book.
    """
    def __init__(self):
        """
        Initialize contact book object with an empty dictionary.
        """
        self.contacts = {}
        
    def add_contact(self, name: str, phone: str, email: str=None):
        """ add a new contact to the contact book

        :param name: the name of the contact
        :param phone: the phone number of the contact
        :param email: the email of the contact, defaults to None
        """
        if name not in self.contacts:
            self.contacts[name]= {'phone': phone, 'email': email}
            print('Contact added successfully!')
        
        else:
            print('Contact already exist!!!')
        
    def view_contacts(self):
        """ view all contacts in the contact book
        """
        for name, info in self.contacts.items():
            print("Name:", name)
            print("Phone:", info['phone'])
            print("Email:", info['email'])
            print('-' * 50)
           
    def delete_contact(self,name: str):
        """ delete a contact from the contact book

        :param name: the name of the contact to be deleted
        """
        if name in self.contacts :
            del self.contacts[name]
            print('Contact deleted successfully')
        else:
            print('Contact not exist!!!')
    
    def update_contact(self, name: str, phone: str=None, email: str=None):
        """ edit a contact in the contact book

        :param name: the name of the contact to be edited
        :param phone: the new phone number of the contact, defaults to None
        :param email: the new email of the contact, defaults to None
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
                
            print('Contact updated successfully!')
            return
        
        print('Contact not found!!!')
        

if __name__ == '__main__':
    book = ContactBook()
    
    while True:
        print('\n--- Contact Book Application ---')
        print('1. Add Contact')
        print('2. Edit Contact')
        print('3. View Contacts')
        print('4. Delete Contact')
        print('5. Quit')
        
        user_choice = input('Please choose an option: ')        
        if user_choice == '1':
            name = input('\nEnter contact name: ')
            phone = input('\nEnter contact phone: ')
            email = input('\nEnter contact email: ')
            book.add_contact(name, phone, email)
        
        elif user_choice == '2':
            name = input('\nEnter contact name: ')
            phone = input('\nEnter contact phone: ')
            email = input('\nEnter contact email: ')
            book.update_contact(name, phone, email)
            
        elif user_choice == '3':
            print('\nList of contacts:\n')
            book.view_contacts()
        
        elif user_choice == '4':
            name = input('\nEnter contact name: ')
            book.delete_contact(name)
            
        elif user_choice == '5':
            print("\nThank You for using Contact Book Application. Goodbye!")
            break
        
        else:
            print("\nInvalid choice! Please try again.")