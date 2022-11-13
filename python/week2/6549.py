from collections import deque       # 스택 ... (반으로 나눠서 왼 오 경계포함 세부분을 재귀로 비교해나가는 방법도 존재)
import sys

while True:
    rec = list(map(int, sys.stdin.readline().split()))
    n = rec.pop(0)

    if n == 0:
        break

    stack = deque()
    answer = 0

    for i in range(n):
        while len(stack) != 0 and rec[stack[-1]] > rec[i]:
            tmp = stack.pop()
            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] -1
            answer = max(answer, width*rec[tmp])
        stack.append(i)

    while len(stack) != 0:
        tmp = stack.pop()

        if len(stack) == 0:
            width=n
        else:
            width = n - stack[-1] -1
        answer = max(answer, width* rec[tmp])
    print(answer)






# import sys        시간초과

# a = 1
# h_list = []

# while a != 0:
#     h_list.append(list(map(int, sys.stdin.readline().split())))
#     a = h_list[-1][0]

# len_h = len(h_list)-1
# ans_list = [0]*len_h

# for i in range(len_h):
#     k = h_list[i]
#     max_rec = 0
#     for x in range(1, k[0]+1):
#         if k[x] != 0:
#             height = k[x]
#             k_list = [x]
#             pl = x
#             pr = x
#             while True:
#                 pl -= 1
#                 if pl == 0: break
#                 if k[pl] >= height:
#                     k_list.append(pl)
#                 else: break
#             while True:
#                 pr += 1
#                 if pr == k[0]+1: break
#                 if k[pr] >= height:
#                     k_list.append(pr)
#                 else: break
#             if len(k_list)*height > max_rec: max_rec = len(k_list)*height
#     ans_list[i] = max_rec

# for a in ans_list:
#     print(a)