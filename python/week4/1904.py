import sys
n = int(sys.stdin.readline())

a = [1, 2]  
if n == 1: print(1)
elif n == 2: print(2)
else:
    for x in range(2, n):
        a.append((a[x-1]+a[x-2])%15746)
    print(a[n-1])