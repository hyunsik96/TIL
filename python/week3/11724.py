import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph=[{0} for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

parent = list(range(n+1))

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

for i in range(1, n+1):
    for k in list(graph[i])[1:]:
        i_root = find(i)
        k_root = find(k)
        if i_root < k_root: parent[k] = parent[i]
        elif i_root > k_root: parent[i] = parent[k]

print(len(set(parent))-1)