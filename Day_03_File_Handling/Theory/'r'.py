
# "r" - READS THE FILE (DEFAULT)
f = open("'r'-demo.txt", "r")

# print(f.read(5))  #print specific chars ✨✨ #(hii+\n+p) -> 5chars

# l1 = f.readline() #print line by line + read invisible '\n' which prints a new empty line with actual line
# print(l1)
# l2 = f.readline()
# print(l2)
# l3 = f.readline() #prints empty line bcoz all data is printed
# print(l3)

print(f.readlines()) # ✨convert lines into LIST

# data = f.read() #read all data
# print(data)


f.close()

        