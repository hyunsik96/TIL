import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

s, x, y = map(int, input().split())
x = x-1
y = y-1

virus = [[0, 0] for _ in range(k)]

for a in range(n):
    for b in range(n):
        if graph[a][b] != 0:
            virus[graph[a][b]-1] = [a, b]

near_vi = [sys.maxsize, 0]

for i in range(k):
    tem_x = x - virus[i][0]
    tem_y = y - virus[i][1]

    if tem_x < 0: tem_x = -1*tem_x
    if tem_y < 0: tem_y = -1*tem_y

    if near_vi[0] > (tem_x + tem_y):
        near_vi[0] = (tem_x + tem_y)
        near_vi[1] = i

if s >= near_vi[0]: print(near_vi[1] + 1)
else: print(0)
