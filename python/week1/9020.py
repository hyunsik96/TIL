import sys
a = int(sys.stdin.readline())
f = []
for x in range(a):
    b = int(input())
    c = int(b/2)
    while True:
        d = 0
        e = 0
        for x in range(2, c):
            if c % x == 0:
                d += 1
                break
        if d == 0:
            for y in range(2, b-c):
                if (b-c) % y == 0:
                    e += 1
                    break
            if e == 0:
                f.append(str(c)+' '+str(b-c))
                break
        c -= 1

for z in f:
    print(z)