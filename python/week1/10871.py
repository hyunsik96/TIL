a, b = input().split()
a = int(a)
b = int(b)
d = []
c = input().split()
for x in range(a):
    if int(c[x]) < b:
        d.append(int(c[x]))

for y in d:
    print(y, end=' ')