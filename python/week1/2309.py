import sys

a = [0]*9
sum = 0

for x in range(9):
    a[x] = int(sys.stdin.readline())

a.sort()

for x in a:
    sum += x


def remove(a, sum):
    for x in range(9):
        b = [a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8]]
        k = sum - b[x] - 100
        del b[x]
        for y in range(8):
            if b[y] == k:
                del b[y]
                return b


answer = remove(a, sum)

for x in answer:
    print(x)
