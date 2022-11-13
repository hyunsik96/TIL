import sys
import heapq

n = int(sys.stdin.readline())
pq = []
ans_list = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if pq: ans_list.append(heapq.heappop(pq))
        else: ans_list.append(0)
    else:
        heapq.heappush(pq, -1*x)

for k in ans_list:
    print(-1*k)





# import sys        시간초과

# n = int(sys.stdin.readline())
# n_list = [int(sys.stdin.readline()) for _ in range(n)]
# x_list = []
# ans_list = []

# for x in n_list:
#     if x == 0:
#         if not x_list: ans_list.append(0)
#         else:
#             ans_list.append(x_list.pop())
#     else:
#         x_list.append(x)
#         x_list.sort()

# for y in ans_list:
#     print(y)