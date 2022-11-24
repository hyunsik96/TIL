import sys

S1 = sys.stdin.readline().strip()
S2 = sys.stdin.readline().strip()
len1 = len(S1)
len2 = len(S2)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])




# import sys                                        # 같은문자오는 등 오류상황 대처 불가

# input = sys.stdin.readline

# a = list(input().rstrip())
# b = list(input().rstrip())

# if len(a) > len(b):
#     c = a
#     a = b
#     b = c

# check = [0]*len(b)

# for aa in a:
#     for i in range(len(b)):
#         if b[i] == aa:
#             if check[i] == check[-1]:
#                 for ii in range(i, len(b)):
#                     check[ii] += 1
#                 break
#             else:
#                 tmp_i = i
#                 while True:
#                     check[tmp_i] += 1
#                     tmp_i += 1
#                     if tmp_i >= len(b) or check[tmp_i] >= check[tmp_i-1]: break

# print(check[-1])