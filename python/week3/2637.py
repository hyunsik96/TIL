import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
queue = deque([])

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append([x, k])
    indegree[x] += 1

ans = [[0]*(n+1) for _ in range(n+1)]
basic = []
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)
        basic.append(i)

while queue:
    now = queue.popleft()
    for i in graph[now]:
        if now in basic:
            ans[i[0]][now] = i[1]
        else:
            for z in range(1, n+1):
                ans[i[0]][z] += ans[now][z]*i[1]
        indegree[i[0]] -= 1
        if indegree[i[0]] == 0: queue.append(i[0])

for num in basic:
    print(f'{num} {ans[n][num]}')







# import sys                                            # 단순히 되돌아가며 재귀로 기본부품 개수 구하여 시간초과
# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# graph = [[] for _ in range(n+1)]
# basic = []

# for _ in range(m):
#     x, y, k = map(int, input().split())
#     graph[x].append([y, k])

# for i in range(1, n):
#     if not graph[i]: basic.append(i)

# ans = [0]*(len(basic))

# def component(c, num):
#     for i in range(len(basic)):
#         if basic[i] == c:
#             ans[i] += num
#             return
    
#     for c_list in graph[c]:
#         component(c_list[0], c_list[1]*num)

# component(n, 1)

# for i in range(len(basic)):
#     print(f'{basic[i]} {ans[i]}')