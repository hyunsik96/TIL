import sys

n = sys.stdin.readline()
cycle = 0

def find_first(a):
    global n
    global cycle

    if int(a) < 10:
        a = '0' + str(int(a))

    b = int(a[0]) + int(a[1])
    cycle += 1

    if b < 10:
        new = a[1] + str(b)
        if int(new) == int(n): return
        else: find_first(new)
    else:
        new = a[1] + str(b)[1]
        if int(new) == int(n): return
        else: find_first(new)

find_first(n)
print(cycle)