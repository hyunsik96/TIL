import sys                                                  # dp 메모리 초과
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

queue = deque([[0, 0]])

while queue:
    now = queue.popleft()
    if now == [n-1, n-1]:
        continue
    x = graph[now[0]][now[1]] + now[0]
    y = graph[now[0]][now[1]] + now[1]
    if x < n:
        dp[x][now[1]] += dp[now[0]][now[1]]
        if [x, now[1]] != [n-1, n-1]:
            queue.append([x, now[1]])
    if y < n:
        dp[now[0]][y] += dp[now[0]][now[1]]
        if [now[0], y] != [n-1, n-1]:
            queue.append([now[0], y])
    dp[now[0]][now[1]] = 0

print(dp[n-1][n-1])



# ans = 0                                           # dfs 시간초과
# def dfs(x, y):
#     global ans

#     if x == n-1 and y == n-1:
#         ans += 1
#         return

#     now = graph[x][y]

#     if now == 0:
#         return
#     if x + now < n:
#         dfs(x + now, y)
#     if y + now < n:
#         dfs(x, y + now)

# dfs(0, 0)
# print(ans)