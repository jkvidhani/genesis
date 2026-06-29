# Clear file first so no empty line appear before data is stored
open("std.txt", "w").close()

def save_std(name,rno,marks):
    with open("std.txt", "a") as f:

    #Method - 1
        f.write(f"{name}, {rno}, {marks}\n")
    #Method - 2
        # f.write(name)
        # f.write(", ")
        # f.write(str(rno))
        # f.write(", ")
        # f.write(str(marks))
        # f.write("\n")
    


def read_std():
    with open("std.txt", "r") as f:
    # METHOD - 1
        data = f.read()
        print(data.strip())
    # #METHOD - 2
    #     lines = f.readlines()  # lines are in list format
    #     for line in lines:
    #         print(line.strip())



def search(name):
    with open("std.txt", "r") as f:

    #METHOD - 1 (just for 'FOUND' or 'Not Found')
        # data = f.read()
        # if name in data:
        #     print("Found!")
        # else:    
        #     print("Not Found!")


    #METHOD - 0 (Advance)
        lines = f.readlines()
        for line in lines:
            if name in line:
                print("Found! - Details :" ,line.strip())

                return       #❤️ if found then exists the functions hence skips else block

        else:
            print("Not Found!")

    
    
    
    
save_std("Hulk",15,500)
save_std("Antman",16,600)
read_std()
search("Hulk")
search("Psuke")