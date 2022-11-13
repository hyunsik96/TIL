import sys

n = int(sys.stdin.readline())

h = [int(sys.stdin.readline()) for _ in range(n)]

ans = 1
max_height = h[n-1]

for x in range(n-2, -1, -1):
    if h[x] > max_height:
        max_height = h[x]
        ans += 1

print(ans)