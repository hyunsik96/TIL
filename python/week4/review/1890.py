import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
def count_path():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                continue

            if i + board[i][j] < N:
                dp[i + board[i][j]][j] += dp[i][j]

            if j + board[i][j] < N:
                dp[i][j + board[i][j]] += dp[i][j]

count_path()
print(dp[N - 1][N - 1])