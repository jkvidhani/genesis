# open("contacts.txt" , "w").close()

class ContactBook:
    def __init__(self):
        self.fn = "contacts.txt"

    def add_contact(self,name ,phn, email):
        with open(self.fn , "a") as f:
            f.write(f"{name}, {phn}, {email}\n")

    def view_contacts(self):
        try:
            with open(self.fn , "r")as f:
                data = f.read()
                print(data)
        except FileNotFoundError:
            print("No contacts yet!")
    
    def search_name(self,name):
        try:
            with open(self.fn , "r") as f:
                data = f.readlines()
                for i in data:
                    if name in i:
                        print("Contact Found:", i)
                        break
                else:
                    print("Contact not found!")
        except FileNotFoundError:
            print("No contacts yet!")
        
    def delete_contact(self,name):
        try:
            with open(self.fn , "r")as f:
                data = f.readlines()

                found = False
                with open(self.fn , "w")as f:
                    for i in data:
                        if name.lower() not in i.lower():
                            f.write(i)
                        else:
                            found = True
                    
                    if found:
                        print(f"{name} deleted!")
                    else:
                        print("Contact not found!")
        except FileNotFoundError:
            print("No contacts yet!")


def main():
    book = ContactBook()
    while True:
        print("\nChoose: 1. Add  2. View  3. Search  4. Delete  5. Exit")
        try:
            choose = int(input("Choose: "))

            if choose == 1:
                name = input("Enter name: ").strip()
                phn = int(input("Enter contact number: "))
                email = input("Enter Email: ").strip()
                book.add_contact(name, phn, email)
                print("Contact added successfully!")
            elif choose == 2:
                print("\nView contacts:")
                with open("contacts.txt", "r")as f:
                    data = f.readlines()
                    c=0
                    for i in data:
                        c+=1
                    if c > 0:
                        print(f"({c}) Contact Found!")
                        book.view_contacts()
                    else:
                        print("No Contacts yet!")
            elif choose == 3:
                name = input("Enter name to search: ").strip()
                book.search_name(name)
            elif choose == 4:
                name = input("Enter name to delete: ").strip()
                book.delete_contact(name)
            elif choose == 5:
                print("Exit Successfully!")
                break
        except ValueError:
            print("Please enter numeric option value only!")


main()




