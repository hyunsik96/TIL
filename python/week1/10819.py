import sys
import itertools

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

nPr = list(itertools.permutations(a, n))

max = 0
b = 0
for x in nPr:
    for y in range(n-1):
        if x[y+1] >= x[y]:
            b += (x[y+1]-x[y])
        else:
            b += (x[y]-x[y+1])
    if b > max: max = b
    b = 0

print(max)