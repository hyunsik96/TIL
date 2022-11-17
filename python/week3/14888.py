import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cal = list(map(int, input().split()))

min_num = sys.maxsize
max_num = -1*sys.maxsize

def calcul(q, w, i):
    if i == 0: return (q+w)
    elif i == 1: return (q-w)
    elif i == 2: return (q*w)
    else:
        if q < 0:
            return -1*(-1*q//w)
        else: return (q//w)

def dfs(num, result):
    global min_num, max_num
    if num == n-1:
        min_num = min(min_num, result)
        max_num = max(max_num, result)
    else:
        for i in range(4):
            if cal[i] != 0:
                cal[i] -= 1
                dfs(num+1, calcul(result, a[num+1], i))
                cal[i] += 1

for i in range(4):
    if cal[i] != 0:
        cal[i] -= 1
        now = calcul(a[0], a[1], i)
        dfs(1, now)
        cal[i] += 1

print(max_num)
print(min_num)