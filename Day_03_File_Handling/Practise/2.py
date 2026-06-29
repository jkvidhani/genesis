with open("G:\Drive G\H C J P\Python\Pyhton OOP\Day_3-File_Handling\Practise\prac.txt", "r") as f:
    data = f.read()
print(data)

num = data.split(",")
print(num)
def countEven():
    c=0
    for i in num:
        if int(i)%2 == 0:
            c+=1
    print("Count of Even:",c)

countEven()


    
    
    

