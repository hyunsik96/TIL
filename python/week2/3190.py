import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
k_list = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
l = int(sys.stdin.readline())
l_list = []

for _ in range(l):
    ll = sys.stdin.readline().split()
    ll[0] = int(ll[0])
    l_list.append(ll)

sec = 0
queue = deque([[1, 1]])
ld = 0  # 0 오 / 1 아 / 2 왼 / 3 위

def kill_snake(next):
    if next in queue: return False
    if next[0] < 1 or next[0] > n or next[1] < 1 or next[1] > n: return False
    return True

while True:
    now = queue[-1]

    for x in l_list:
        if x[0] == sec:
            if x[1] == 'L':
                if ld == 0: ld = 3
                else: ld = ld - 1
            else:
                if ld == 3: ld = 0
                else: ld = ld + 1
            break

    sec += 1

    if ld == 0:
        now = [now[0], now[1]+1]
        if kill_snake(now):
            queue.append(now)
        else: break
        if now not in k_list: queue.popleft()
        else: k_list.remove(now)
    elif ld == 1:
        now = [now[0]+1, now[1]]
        if kill_snake(now):
            queue.append(now)
        else: break
        if now not in k_list: queue.popleft()
        else: k_list.remove(now)
    elif ld == 2:
        now = [now[0], now[1]-1]
        if kill_snake(now):
            queue.append(now)
        else: break
        if now not in k_list: queue.popleft()
        else: k_list.remove(now)
    else:
        now = [now[0]-1, now[1]]
        if kill_snake(now):
            queue.append(now)
        else: break
        if now not in k_list: queue.popleft()
        else: k_list.remove(now)

print(sec)