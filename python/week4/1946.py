import sys
from heapq import heappop, heappush
input = sys.stdin.readline

t = int(input())
ans_list = [1]*t

for i in range(t):
    num = int(input())
    test = []

    for _ in range(num):
        heappush(test, list(map(int, input().split())))

    last = heappop(test)

    while test:
        tmp = heappop(test)
        if tmp[0] < last[0] or tmp[1] < last[1]:
            last = tmp
            ans_list[i] += 1

print(*ans_list, sep='\n')





# import sys                                # 시간초과
# input = sys.stdin.readline

# t = int(input())
# ans_list = [0]*t

# for i in range(t):
#     num = int(input())
#     test_case = [list(map(int, input().split())) for _ in range(num)]
#     ans_list[i] = num
#     test_case.sort(key= lambda x: x[0]+x[1])

#     for ti in range(0, num):    # 합이 작은 test_case의 인덱스 ti 부터 확인
#         for k in range(0, ti):
#             if test_case[ti][0] > test_case[k][0] and test_case[ti][1] > test_case[k][1]:
#                 ans_list[i] -= 1
#                 break

# print(*ans_list, sep='\n')