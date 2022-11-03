import sys
input = sys.stdin.readline
N = int(input().rstrip())
global cnt
cnt = 0
def cycle(n):
    global cnt
    if n < 10:
        a = 0
        b = n
    else:
        a = n // 10
        b = n % 10
    if a + b >= 10:
        c = (a + b) % 10
    else:
        c = a + b
    new_n = b * 10 + c
    cnt += 1
    if new_n == N:
        print(cnt)
        return
    cycle(new_n)




cycle(N)