# 가장 가까운 경로를 찾는 것임으로 같은 레벨, 즉 넓이를 우선 탐색해가며 도착하면 끝내버리면 된다.

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def check(a, b):
    global n, m
    able = []
    if a > 0 and graph[a-1][b] == 1 and visited[a-1][b] == 0: able.append((a-1, b))
    if b > 0 and graph[a][b-1] == 1 and visited[a][b-1] == 0: able.append((a, b-1))
    if a < (n-1) and graph[a+1][b] == 1 and visited[a+1][b] == 0: able.append((a+1, b))
    if b < (m-1) and graph[a][b+1] == 1 and visited[a][b+1] == 0: able.append((a, b+1))
    return able

queue = deque([(0,0)])
visited[0][0] = 1

while queue:
    x, y = queue.popleft()

    if x == n-1 and y == m-1:
        print(visited[x][y])
        break
    
    for k in check(x, y):
        visited[k[0]][k[1]] = visited[x][y] + 1
        queue.append(k)






# import sys                        # dfs 시간초과

# input = sys.stdin.readline

# n, m = map(int, input().split())

# graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
# visited = [[False]*m for _ in range(n)]
# min_ans = 20000
# ans = 0
# def check(a, b):
#     global n, m
#     able = []
#     if a > 0 and graph[a-1][b] == 1 and visited[a-1][b] == False: able.append([a-1, b])
#     if b > 0 and graph[a][b-1] == 1 and visited[a][b-1] == False: able.append([a, b-1])
#     if a < (n-1) and graph[a+1][b] == 1 and visited[a+1][b] == False: able.append([a+1, b])
#     if b < (m-1) and graph[a][b+1] == 1 and visited[a][b+1] == False: able.append([a, b+1])
#     return able

# def dfs(a, b):
#     global n, m, min_ans, ans
#     visited[a][b] = True
#     ans += 1
#     if a == n-1 and b == m-1:
#         min_ans = min(min_ans, ans)
#         return
#     else:
#         for x in check(a, b):
#             dfs(x[0], x[1])
#             visited[x[0]][x[1]] = False
#             ans -= 1

# dfs(0, 0)
# print(min_ans)