import sys
from collections import deque
input = sys.stdin.readline

# 점 개수, 선 개수, 시작 점
n, m, v = map(int, input().split())

graph=[{0} for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

dfs_list = []
bfs_list = []

def dfs(num):
    dfs_list.append(num)
    check[num] = True

    for k in sorted(list(graph[num])[1:]):
        if not check[k]:
            dfs(k)

def bfs(root):
    queue = deque([root])
    bfs_list.append(root)
    check[root] = True
    while queue:
        now = queue.popleft()
        for k in sorted(list(graph[now])[1:]):
            if not check[k]:
                bfs_list.append(k)
                check[k] = True
                queue.append(k)

check = [False]*(n+1)
dfs(v)
check = [False]*(n+1)
bfs(v)
print(*dfs_list)
print(*bfs_list)