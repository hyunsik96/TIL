import sys

n = int(sys.stdin.readline())

a = [0]*10001

for x in range(n):
    a[int(sys.stdin.readline())-1] += 1

for y in range(10001):
    if a[y] != 0:
        for z in range(a[y]):
            print(y+1)