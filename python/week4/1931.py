import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
time_table = []

for _ in range(n):
    a, b = map(int, input().split())
    heappush(time_table, [b, a])

end_time = 0
ans = 0

while time_table:
    tmp = heappop(time_table)
    if tmp[1] >= end_time:
        end_time = tmp[0]
        ans += 1

print(ans)