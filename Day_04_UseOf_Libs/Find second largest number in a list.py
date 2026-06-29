l = list(map(int,input().split()))  # noqa: E741
mx=l[0]
mn=mx

for i in l:
    if i>mx :
        mn = mx
        mx = i
    if i>mn and i!=mx:
        mn = i
    
print(mx)
print(mn)