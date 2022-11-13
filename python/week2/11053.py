import sys

n = int(sys.stdin.readline())

a_list = list(map(int, sys.stdin.readline().split()))

ans_list = [1 for _ in range(n)]

for x in range(n):
    for y in range(x):
        if a_list[y] < a_list[x] and ans_list[y] >= ans_list[x]:
            ans_list[x] = ans_list[y] + 1

print(max(ans_list))