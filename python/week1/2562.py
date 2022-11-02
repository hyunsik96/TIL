a = []
for z in range(9):
    a.append(int(input()))
b = 1
c = 1
for x in range(9):
    if a[x] > b:
        b = a[x]
        c = x
print(b)
print(c+1)

