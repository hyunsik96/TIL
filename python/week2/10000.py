


# import sys                    원 속에 접하지 않는 원과 밖 원에 접하면 두개와 접해도 공간이 2개 추가분할되지 않음... ㄲㅂ
# import bisect

# n = int(sys.stdin.readline())

# c_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# ans = 1

# x_list = []

# def binary_search(num):
#     if x_list:
#         pl = 0
#         pr = len(x_list)-1
#         while pl < pr:
#             center = (pl+pr)//2
#             if x_list[center] < num: pl = center+1
#             else: pr = center
#         if x_list[pl] == num: return True
#         else: return False
#     else: return False

# for c in c_list:
#     check = 0
#     if binary_search(c[0]+c[1]): check += 1
#     else: bisect.insort(x_list, c[0]+c[1])
#     if binary_search(c[0]-c[1]): check += 1
#     else: bisect.insort(x_list, c[0]-c[1])
#     if check == 2: ans += 2
#     else: ans += 1

# print(ans)