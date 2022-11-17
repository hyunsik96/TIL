import sys
from collections import deque

input = sys.stdin.readline

# 도시, 도로, 거리, 출발
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
level = [-1]*(n+1)
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque([x])
level[x] = 0

while queue:
    now = queue.popleft()

    if level[now] == k+1: break

    for a in graph[now]:
        if level[a] == -1:
            level[a] = level[now] + 1
            queue.append(a)
            if level[a] == k: ans.append(a)

if ans:
    ans.sort()
    print(*ans, sep='\n')
else: print(-1)