import sys

n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
stack = []
ans_list=[0]*n

for x in range(n):
    while stack and tower[x] >= tower[stack[-1]]:
        stack.pop()
    if stack:
        ans_list[x] = stack[-1] + 1
    stack.append(x)

for y in ans_list:
    print(y, end=' ')



# import sys        시간초과

# n = int(sys.stdin.readline())

# tower = list(map(int, sys.stdin.readline().split()))

# ans_list = [0]*n

# for x in range(1, n):
#     for y in range(x-1, -1, -1):
#         if tower[y] > tower[x]:
#             ans_list[x] = y+1
#             break

# for z in ans_list:
#     print(z, end=' ')



# import sys       실수로 최대만 마주치는 줄 암

# n = int(sys.stdin.readline())

# tower = list(map(int, sys.stdin.readline().split()))
# max_tower = [0]*n
# ans_list = [0]*n

# for x in range(1, n):
#     if tower[x] >= tower[max_tower[x-1]]: max_tower[x] = x
#     else: max_tower[x] = max_tower[x-1]

# for x in range(1, n):
#     if tower[x] < tower[max_tower[x-1]]: ans_list[x] = max_tower[x-1] +1

# for z in ans_list:
#     print(z, end=' ')