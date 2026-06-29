s1 = input()
s2 = input()

l1 = sorted(s1)
l2 = sorted(s2)

k1=[]
v1=[]
for i in l1:
    if i not in k1:
        k1.append(i)
        v1.append(s1.count(i))

k2=[]
v2=[]
for i in l2:
    if i not in k2:
        k2.append(i)
        v2.append(s2.count(i))

d1 = dict(zip(k1,v1))
d2 = dict(zip(k2,v2))

print(d1==d2)


