import sys

n, r, q = map(int, sys.stdin.readline().split())

a = 2 ** n
b = q + 1
c = r + 1
d = -1 # 저장용

def get(x, y, z):               # 몇 행, 몇 열, 변의 길이
    global d
    if z != 2:
        if x <= z/2 and y <= z/2:   # 왼위
            get(x, y, z/2)
        if x > z/2 and y <= z/2:    # 오위
            d += ((z/2) ** 2)
            get(x-z/2, y, z/2)
        if x <= z/2 and y > z/2:    # 왼아
            d += ((z/2) ** 2)*2
            get(x, y-z/2, z/2)
        if x > z/2 and y > z/2:     # 오아
            d += ((z/2) ** 2)*3
            get(x-z/2,y-z/2,z/2)
    
    else:
        if x == 1 and y == 1: d += 1
        if x == 2 and y == 1: d += 2
        if x == 1 and y == 2: d += 3
        if x == 2 and y == 2: d += 4

get(b, c, a)
print(int(d))