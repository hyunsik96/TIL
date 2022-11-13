import sys

n, c = map(int, sys.stdin.readline().split())

x_list = [int(sys.stdin.readline()) for _ in range(n)]

x_list.sort()

max_num = 1

def gong_u(n, c, num):
    current = x_list[0]
    count = 1
    for i in range(1, len(x_list)):
        if x_list[i] >= current + num:
            count += 1
            current = x_list[i]

    if count>=c: return True
    else: return False

def binary_search(start, end):
    global n
    global c
    center = (start + end) // 2
    if end - start > 1:
        if gong_u(n, c, center):
            binary_search(center, end)
        else:
            binary_search(start, center-1)
    elif start+1 == end:
        if gong_u(n, c, end):
            print(end)
        else: print(start)
    else: print(start)

binary_search(1, (x_list[n-1]-x_list[0])//(c-1))



# import sys            재귀없는 이진탐색

# n, c = map(int, sys.stdin.readline().split())

# array = [int(sys.stdin.readline()) for _ in range(n)]

# array.sort()


# def binary_search(array, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         current = array[0]
#         count = 1

#         for i in range(1, len(array)):
#             if array[i] >= current + mid:
#                 count += 1
#                 current = array[i]

#         if count >= c:
#             global answer
#             start = mid + 1
#             answer = mid
#         else:
#             end = mid - 1

# # 최소거리
# start = 1
# # 최대거리
# end = array[-1] - array[0]

# answer = 0

# binary_search(array, start, end)
# print(answer)






# import sys                시간초과

# n, c = map(int, sys.stdin.readline().split())

# x_list = [int(sys.stdin.readline()) for _ in range(n)]

# x_list.sort()

# max_num = 1

# def gong_u(n, c, num):
#     c_list = [True]*c
#     c_list[0] = x_list[0]
#     for k in range(1, c):
#         for x in range(k, n):
#             if x_list[x] - c_list[k-1] >= num:
#                 c_list[k] = x_list[x]
#                 break
#     if c_list[c-1] == True: return False
#     else: return True

# def binary_search(start, end):
#     global n
#     global c
#     center = (start + end) // 2
#     if end - start > 1:
#         if gong_u(n, c, center):
#             binary_search(center, end)
#         else:
#             binary_search(start, center-1)
#     elif start+1 == end:
#         if gong_u(n, c, end):
#             print(end)
#         else: print(start)
#     else: print(start)

# binary_search(1, (x_list[n-1]-x_list[0])//(c-1))