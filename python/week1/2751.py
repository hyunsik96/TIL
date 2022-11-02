import sys

a = int(sys.stdin.readline())
b = []
for x in range(a):
    b.append(int(sys.stdin.readline()))

b.sort()

for y in b:
    print(y)