# Create a new file "practice.txt" using python. Add the following data in it:

# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

# WAF that replace all occurrences of "java" with "python" in above file.
# Search if the word "learning" exists in the file or not.

with open(
    "G:\Drive G\H C J P\Python\Pyhton OOP\Day_3-File_Handling\Practise\practice.txt","w",) as f:

    f.write(
        "Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
    
def replace():
    with open(
        "G:\Drive G\H C J P\Python\Pyhton OOP\Day_3-File_Handling\Practise\practice.txt","r",) as f:

        data = f.read()

    new_data = data.replace("Java", "Python")


    with open(
        "G:\Drive G\H C J P\Python\Pyhton OOP\Day_3-File_Handling\Practise\practice.txt","w",) as f:

        f.write(new_data)

def findWord():
    with open("G:\Drive G\H C J P\Python\Pyhton OOP\Day_3-File_Handling\Practise\practice.txt", "r") as f:

        data = f.read()
        word = input()
        if word in data:
            print("Found!")
        else:
            print("Not Found!")

    
# replace()
# findWord()


def findLine():
    with open("G:\Drive G\H C J P\Python\Pyhton OOP\Day_3-File_Handling\Practise\practice.txt", "r") as f:

        word = input()
        data = True
        line = 1

        while(data): #or while(data ==  True):
            data = f.readline()
            if word in data:
                print("Found",word, "in line :",line)
                return
            line+=1

    return print(-1)

findLine()




        






