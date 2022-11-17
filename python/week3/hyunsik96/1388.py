import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, list((input().rstrip()).replace('-', '1').replace('|', '2')))) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

ans = 0

for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            if graph[x][y] == 1:
                a = x
                b = y
                while graph[a][b] == 1:
                    visited[a][b] = True
                    b = b + 1
                    if b == m: break
                ans += 1
            else:
                a = x
                b = y
                while graph[a][b] == 2:
                    visited[a][b] = True
                    a = a + 1
                    if a == n: break
                ans += 1

print(ans)