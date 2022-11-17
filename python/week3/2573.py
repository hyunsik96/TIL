import sys
from copy import deepcopy
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def tran(a, b, tem):
    if tem[a-1][b] != 0 and tem[a-1][b] != -1:
        tem[a-1][b] = -1
        tran(a-1, b, tem)
    if tem[a][b-1] != 0 and tem[a][b-1] != -1:
        tem[a][b-1] = -1
        tran(a, b-1, tem)
    if tem[a+1][b] != 0 and tem[a+1][b] != -1:
        tem[a+1][b] = -1
        tran(a+1, b, tem)
    if tem[a][b+1] != 0 and tem[a][b+1] != -1:
        tem[a][b+1] = -1
        tran(a, b+1, tem)

def is_two():
    global n, m
    tem = deepcopy(graph)
    for a in range(1, n):
        for b in range(1, m):
            if tem[a][b] != 0:
                tem[a][b] = -1
                tran(a, b, tem)
                for c in range(1, n):
                    for d in range(1, m):
                        if tem[c][d] != 0 and tem[c][d] != -1:
                            return True # 두 덩어리 이상
                return False # 한 덩어리

def zero_num(a, b, tem2):
    global n, m
    num = 0
    if tem2[a-1][b] == 0: num += 1
    if tem2[a][b-1] == 0: num += 1
    if tem2[a+1][b] == 0: num += 1
    if tem2[a][b+1] == 0: num += 1
    return num

def next_year():
    global n, m
    is_change = 0
    tem2 = deepcopy(graph)
    for a in range(1, n):
        for b in range(1, m):
            if tem2[a][b] != 0:
                graph[a][b] = max((tem2[a][b] - zero_num(a, b, tem2)), 0)
                is_change += 1
    return is_change # 0이 리턴되면 변경사항 없음 -> 다 0

ans = 0

while True:
    if next_year() != 0:
        ans += 1
        if is_two():
            print(ans)
            break
    else:
        print(0)
        break