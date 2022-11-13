import sys

n = int(sys.stdin.readline())

w_list = list(map(int, sys.stdin.readline().split()))

w_list.sort()

if w_list[0] >= 0:
    print(w_list[0], end=' ')
    print(w_list[1])
elif w_list[n-1] <= 0:
    print(w_list[n-2], end=' ')
    print(w_list[n-1])
else:
    ans = 2000000000
    ans_list = []
    pl = 0
    pr = n-1
    while pl < pr:
        left = w_list[pl]
        right = w_list[pr]
        if abs(left+right) <=ans:
            ans_list = [left, right]
            ans = abs(left+right)
        if left+right > 0:
            pr -= 1
        elif left+right < 0:
            pl += 1
        else: break
    print(ans_list[0], end=' ')
    print(ans_list[1])


# import sys                          # 메모리 초과
# from itertools import combinations

# n = int(sys.stdin.readline())

# w_list = list(map(int, sys.stdin.readline().split()))
# if w_list[0] >= 0:
#     print(w_list[0], end=' ')
#     print(w_list[1])
# elif w_list[n-1] <= 0:
#     print(w_list[n-2], end=' ')
#     print(w_list[n-1])
# else:
#     c_list = list(combinations(w_list, 2))
#     a_list = [1000000000, 1000000000]

#     for x in c_list:
#         if sum(x)**2 <= sum(a_list)**2:
#             a_list = x

#     if a_list[0] >= a_list[1]:
#         print(a_list[1], end=' ')
#         print(a_list[0])
#     else:
#         print(a_list[0], end=' ')
#         print(a_list[1])