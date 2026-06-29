#Syntax - 1
f = open("'r'-demo.txt", "r")
print(f.read())
f.close()

#Syntax - 2
with open("'r'-demo.txt", "r") as f:
    print(f.read())