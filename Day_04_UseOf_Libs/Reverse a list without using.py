s= input()
k= list(s)

for i in range(len(k)):
    c = k.pop()
    k.insert(i,c)

x = "".join(k)
print(x)

