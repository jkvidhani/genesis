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

if __name__ == "__main__":
    print("Hi")
    print("Ciao")
    
