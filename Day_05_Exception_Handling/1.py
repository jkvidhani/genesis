# Clear file before starting
open("std.txt", "w").close()

def std(name,rno,marks):

    if marks < 0 or marks > 100:
        raise ValueError("Invalid")
    if not name.isalpha():
        raise ValueError("Invalid")
    
    with open("std.txt", "a") as f:
        f.write(f"{name}, {rno}, {int(marks)}\n")
        

def showData():
    try:
        with open("std.txt", "r") as f:
            data = f.read()
            print(data)

    except FileNotFoundError:
        print("No std file found!")


try:
    marks = int(input())
except ValueError:
    print("Enter valid value")

try:
    std("Hulk","15",marks)
except ValueError as e:
    print(e)
showData()

    