a = int(input())
b = int(input())
c = int(input())
d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(len(str(a*b*c))):
    d[int(str(a*b*c)[x])] += 1

for y in d:
    print(y)