import sys                                                  # dfs 시간초과
sys.setrecursionlimit(1100)
input = sys.stdin.readline

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[True]*n for _ in range(m)]
visited[0][0] = False
ans = 0

def dfs(x, y):
    global ans

    if x == m-1 and y == n-1:
        ans += 1
        return
    
    if 0 <= x-1 < m and visited[x-1][y] and graph[x][y] > graph[x-1][y]:
        visited[x-1][y] = False
        dfs(x-1, y)
        visited[x-1][y] = True

    if 0 <= x+1 < m and visited[x+1][y] and graph[x][y] > graph[x+1][y]:
        visited[x+1][y] = False
        dfs(x+1, y)
        visited[x+1][y] = True

    if 0 <= y-1 < n and visited[x][y-1] and graph[x][y] > graph[x][y-1]:
        visited[x][y-1] = False
        dfs(x, y-1)
        visited[x][y-1] = True

    if 0 <= y+1 < n and visited[x][y+1] and graph[x][y] > graph[x][y+1]:
        visited[x][y+1] = False
        dfs(x, y+1)
        visited[x][y+1] = True

dfs(0, 0)
print(ans)