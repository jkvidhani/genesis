from contact_book import ContactBook

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


if __name__ == "__main__" :
    main()