import sys
from math import sqrt
input = sys.stdin.readline

N, M = map(int, input().split())

dp = [[float('inf')]*(int(1.5*(N**0.5) + 2)) for _ in range(N+1)]       # 1 ~ n 번 인덱스의 n개 돌 (연산을 줄이기 위한 최대 점프속도 계산)
dp[1][0] = 0                                                                                      # 1번 돌의 초기 도착 0 속도 최소 점프 수
trap = set()        # 못밟는 돌
for _ in range(M):
    trap.add(int(input()))

for i in range(2, N+1):
    if i in trap:
        continue
    for v in range(1, int(sqrt(2*i))+1):                                                # i번째 돌 까지 가장 빠르게 올 수 있는 속도
        dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1

result = min(dp[N])
if result == float('inf'):
    print(-1)
else:
    print(result)









# import sys                                                # 최소로 해당 돌에 도착하는 경우를 생각했지만, 도착하는 속도를 동시에 생각 못함
# input = sys.stdin.readline

# n, m = map(int, input().split())

# rock_tf = [True]*n
# inf = 10001

# for _ in range(m):
#     tmp = int(input())
#     rock_tf[tmp-1] = False

# now = 0     # 현재 돌
# ans = 0       # 최소 점프 횟수
# jump = 1    # 도착 점프 거리

# dp = [[0, 1] for _ in range(n)]     # i 번째 인덱스 돌에 [최소 점프 횟수, 도착한 점프 거리]
# check = [False]*n                        # i 번쨰 인덱스의 최소 점프 횟수가 구해졌는지 여부
# check[0] = True                           # 첫 돌 체크

# def dfs(i):
#     if check[i]:                               # 이미 구해졌다면 그 값 리턴
#         return dp[i]
#     # if not rock_tf[i]:                      # i가 도착 불가한 돌이라면 inf, 1 리턴
#     #     dp[i] = [inf, 1]
#     #     return dp[i]

#     tmp_min = [inf, 1]
#     for a in range(i):
#         tmp_dfs = dfs(a)
#         if i - a == tmp_dfs[1]:
#             if tmp_dfs[0] + 1
#             return [tmp_dfs[0]+1, tmp_dfs[1]]
#         elif i - a == dfs(a)[1] + 1:
#             return [tmp_dfs[0]+1, tmp_dfs[1]]
#         elif i - a == dfs(a)[1] - 1:
#             return [tmp_dfs[0]+1, tmp_dfs[1]]