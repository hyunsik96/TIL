import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(1 << n-1) for _ in range(n)]                                     # 0 번 도시 시작으로 정했으니 0번 경우 빼고 n-1

def dfs(i, visited):
    if dp[i][visited] != 0:          # 이미 기입 됐으면 기입된 값 리턴
        return dp[i][visited]
    
    if visited == (1 << n-1) - 1:
        if graph[i][0]:                 # 모든 도시를 방문했을  때 현재 도시에서 0 번 도시로 갈 수 있다면 그 비용 리턴
            return graph[i][0]
        else:
            return float('inf')       # 갈 수 없다면 비용 무한대 리턴
    
    min_route = float('inf')

    for j in range(1, n):
        if not graph[i][j]:            # 현재 도시에서 1~n-1 번 도시로 갈 수 없다면
            continue
        if visited & (1 << j-1):     # 이진수로 j-1 번 째 칸 (j번째 도시 방문여부) 가 visited 에 이미 찍혀있다면
            continue
        d = graph[i][j] + dfs(j, visited | (1 << j-1))      # ( 현재 도시에서 j 번째 도시로 가는 비용 ) +
                                                                                # ( 현재 방문여부에 j 찍고 j 번째 도시로 이동했을 때 남은 최소 비용 )
        if min_route > d:
            min_route = d           # 현재 도시에서 갈 수 있는 도시들 j 에서 위의 값중 가장 작은 d 를 주는 비용이 현 dfs(i, visited)
        
    dp[i][visited] = min_route

    return min_route

print(dfs(0, 0))




# import sys
# input = sys.stdin.readline
# inf = 16000001

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# dp = [[inf]*(1 << n) for _ in range(n)]

# # 순환 경로이기에 한 경우가 출발지점에 따라 n가지로 나뉜다. (출발지점 정해도 무방)

# def dfs(x, visited):
#     if visited == (1 << n) - 1:     # 모든 도시를 방문했는지
#         if graph[x][0]:     # 첫 도시로 돌아갈 수 있다면
#             return graph[x][0]
#         else:
#             return inf
    
#     if dp[x][visited] != inf:       # 최소비용 이미 계산된 경우
#         return dp[x][visited]
    
#     for i in range(1, n):
#         if not graph[x][i]:     #  i 로 이동이 불가능할 때
#             continue
#         if visited & (1 << i):  # 둘이 같은 자리에 1인 부분이 있는지 == 방문했는지
#             continue

#         dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])

#     return dp[x][visited]

# print(dfs(0, 1))