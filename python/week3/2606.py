# 각 노드에서 find를 통해 최소 조상을 찾고, 떨어진 두 노드를 연결할 때 작은 값을 부여한다.
# union 과정에서 연결하는 두 노드의 값만 최신화하기에 연결된 값들은 다시 find 로 불러 확인해야 업데이트 가능하다.

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

parent = list(range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

ans = -1

for x in parent:
    if find(x) == 1: ans += 1

print(ans)