class Contact:
    def __init__(self,name,phone_number,email):
        self.name=name
        self.phone_number=phone_number
        self.email=email

class ContactBook:
    def __init__(self):
        self.contacts = [
            Contact("Alice", "1234567890", "alice@email.com"),
            Contact("Bob", "9876543210", "bob@email.com")
        ]

    def add_contact(self, name, phone_number, email):
        new_contact=Contact(name,phone_number,email)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully., phone number is {phone_number}, email is {email}")

    def display_all_contacts(self):
         if self.contacts:
            print("All Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
         else:
          print("No contacts found.")

    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name== name:
                print(f"found contact {contact.name},{contact.phone_number},{contact.email}")
                return contact
        else:
                print("contact not found")

    def update_contact(self, name, new_name=None, new_phone_number=None,new_email=None):
            contact=self.search_contact(name)
            if contact:
                if new_name:
                    contact.name=new_name
                if new_phone_number:
                    contact.phone_number=new_phone_number
                if new_email:
                    contact.email=new_email
                print(f"contact for {name} has been updated to {contact.name, contact.phone_number, contact.email}")
                return contact
            else:
                print("no contact found with given name")   

    def delete_contact(self,name):
        contacts=self.search_contact(name)
        if contacts:
            self.contacts.remove(contacts)
            print(f"{contacts.name} has been removed")
        else:
            print("contact not found with given name") 

        
def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add New Contact")
        print("2. Display contacts book")
        print("3. Search contacts book")
        print("4. Update contacts book")
        print("5. Remove contact from contacts book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)
        elif choice == "2":
            contact_book.display_all_contacts()
        elif choice == "3":
            name=input("please enter contact name").capitalize().strip()
            contact_book.search_contact(name)
        elif choice == "4":
            name=input("type in original contact name (or leave blank if you dont want to change)")
            new_name=input("type in update contact name (or leave blank if you dont want to change name)")
            new_phone_number=input("type in new number (or leave blank if you dont want to change number )")
            new_email=input("type in new email(or leave balnk if you dont want to change email)")
            contact_book.update_contact(name,new_name or None, new_phone_number or None, new_email or None)   
        elif choice == "5":
            name=input("enter name you want to delete").capitalize().strip()
            contact_book.delete_contact(name)         
        elif choice == "0":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("incorrect user choice please try again")

if __name__ == "__main__":
    main()

#!line1-5- i created a new class called Contact. then initialized the object that was created with a name, phone number and email which are my parameters. 
#todo i the created new variable names and assigned them to the parameters that i have used. 

#!line7-12- i created a new class called ContactBook. 
#! then i initialized the object that was created with self which is my parameter. 
#todo i then created a new variable and assigned to a list that was made with the different people's contact deatails.

#* line 14-17-i was able to add a new contact to my contact book using a method called add_contact method. i then created a new variable and then assigned it to the contact class with it's different parameters. 
#todo i created craig's info by creating a new contact variable called new_contact with craigs deatils in.
#* then used the append method so that i could add the new contact into the the contact book original list. 
#~then printed an f string confirming that craig and his deatils have been added to the list using {}

#*line 19-25- i was able to display the contacts into the termianl by using self.contacts as my parmeter and then i used for loop to find the variable from my variable lists which is self.contacts so the the programme knows which variables too look for in the list that i called for. then used the print statment to display the contacts in the terminal using an f string and {} with it's parameters inside.

#*line 27-33- i was able to search for the individual contat in the list by creating a new def  which will search for a contact by name, phone number, or email
#?then i used a for loop to find my contacts within the seleceted list so that it will run once if either correct or incorrect answer given. 
#?then used an if statement to see if the statment that i have provided is true because if its true it should run then created the variable contact.name==name to see if it mataches the parameter that is defined under name. 
#~then used a print statment and f string so that it would print in the terminal that the name provided has been found using {} then used the return keyword.
#? also used an else statement so that if incorrect info was put into the terminal which will print the else statment.

#*line 35-47- i was able to update the contact details given from the original list by using the def function which will update the contact book.
#todothen i created a new variable called contact=self.search_contact(name) using an assignment operator so that the variable matches/
#?line38-43- i created an if statement so that i could write out the new name,number and email statements#
#~then i created a print statment with an f string to print out the code with the new infomation if it was provided and changed it to the new contact details using {} and added in contact.name,contact.phone_number and contact.email inside and then used the return keyword.
#?then used an else statment if an original contact name wasnt provided

#*line49-55- i was able to delete contacts from the contacts list by using a def function eg def delete_contact(self,name) which displays all the contacts in the contact book.
#todo i then created a new variable called contacts.self.search_contact(name)
#?then created a if statement
#*then i used the .remove method so that i could remove the name from the list depending on which name i wrote into the terminal.
#~then used a print function and f string so that it would print out that it removed the contact that i had given because i added contacts between {}

#!line58-59- I demonstarted the different uses by using def main()
#todo i created a new variable called contact_book and assigned it to the ContactBook using =.

#?line 61-68- creates an infinite loop. The condition True always evaluates to True, so the loop will run indefinitely.
#~ i then created seperate print statements which will display the menu 

#todoline70- I created a new variable called choice and then used an input function so that the user can type in a number into the termianl between 0-5
#~ it will then print out the corresponding print statement depening on what was wrote into the terminal

#?72-95- i created 4 new elif statements so that when i had given an option between 0-5 in the first options, it would then go to the specific number
# ~ then print out a new statement giving out the new options of either typing the write name will print out the if statement when in the specific list eg if i choose option 4 it would go to the updat_contact function and then i would provide it with info. if i gave new info it would print out the new info in the termianl, if i just clicked enter through all the options it would keep the origianl contact. 
# ~if i didnt give a correct name it would print the else statement.

#?line 93- i used the break keyword to break the for loop.

#?line 104-105 i created an else statment to that if i provided incorrect info (not using 0-5) it will print out the print statement

# ?line 106-107- i created to check if the script is being run directly (as opposed to being imported as a module in another script). If true, it calls the main function. This ensures that the code inside main only runs when the script is executed directly


# i used chatgpt to run my original code that i worte out to see if there were any errors or if it was readable. i had to update the def statements so that they all alligned with eachother because originally the code wasn't running so i put it into chatgpt and it came up with make sure all the def statements match.

#! is the classes and initialized parts with it's parameters
#* is for the def methods used and it's parameters
#todo is for the variable names
#? is for the if statments and for loop and breaks,returns
#~ is for the print statments