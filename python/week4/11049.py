import sys

input = sys.stdin.readline

n = int(input())

n_list = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

# 아래 3줄 설정으로 좌상단, 우하단을 가로지르는 중앙 대각선부터 오른쪽으로 순차적 탐색
for d in range(1, n):
    for i in range(n-d):
        j = i + d
    
        if d == 1:
            dp[i][j] = n_list[i][0] * n_list[j][0] * n_list[j][1]
            continue
        
        dp[i][j] = float('inf')

        # i~j의 합을 i~k, k+1~j 로 나누어 이 구간 합과 두 구간을 곱할때 값을 합하여 비교
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + n_list[i][0] * n_list[k][1] * n_list[j][1])

print(dp[0][-1])