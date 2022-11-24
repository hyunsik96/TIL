import sys

input = sys.stdin.readline

n, k = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
ans_list = [[0]*(k+1) for _ in range(n+1)]

for xi in range(0, n):
    for i in range(1, k+1):
        if i >= wv[xi][0] and ans_list[xi][i-wv[xi][0]] + wv[xi][1] > ans_list[xi][i]:
            ans_list[xi+1][i] = ans_list[xi][i-wv[xi][0]] + wv[xi][1]
        else:
            ans_list[xi+1][i] = ans_list[xi][i]

print(ans_list[n][k])