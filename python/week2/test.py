import sys

n = int(sys.stdin.readline())
safety = [None] * n

for i in range(n):
    safety[i] = list(map(int, sys.stdin.readline().split()))

# flag = [[False] *n]*n
# o = [False] *n
flag = [[]*n]*n
# for i in range(n):
#     flag.append(o)

rain = 5

print(flag)

# for d in range(n):
#     for k in range(n):
#         if safety[d][k] > rain:
#             print(str(safety[d][k])+', d: '+str(d)+', k: '+str(k))
#             flag[d][k] = True
#             print(flag[d][k])
flag[0][0] = True
print(flag)
area = [[True]*n for bfde in range(n)]
print(area)