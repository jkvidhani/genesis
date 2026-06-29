#Using List concept for dict's output
d1 = eval(input())
d2 = eval(input())

k=[]
v=[]
vs=0
for key in d1:
    k.append(key)
    if key in d2:
        vs = d1[key] + d2[key]
        v.append(vs)
    else:
        v.append(d1[key])

for key in d2:
    if key not in k:
        k.append(key)
        v.append(d2[key])

dic = dict(zip(k,v))
print(dic)
        

