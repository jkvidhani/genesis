d = eval(input())
x=""
v=0
for key in d:
    if d[key]>v:
        v = d[key]
        x = key
print(f" {x}: {v}")

    