l = list(map(int,input().split()))  # noqa: E741

def avg():
    s=0
    for i in l:
        s+=i
    print(s/len(l))

def max():
    mx=l[0]
    for i in l:
        if i>mx:
            mx=i
    print(mx)

def min():
    mn=l[0]
    for i in l:
        if i<mn:
            mn=i
    print(mn)

avg()
min()
max()