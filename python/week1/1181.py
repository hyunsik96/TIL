import sys

n = int(sys.stdin.readline())

list=[]

def common(h):
    global list
    for x in list:
        if x == h: return False
    return True

for x in range(n):
    k = sys.stdin.readline().strip()
    if common(k):
        list.append(k)

list2 = []
for i in list:
    list2.append((len(i), i))

result = sorted(list2)

for a, b in result:
    print(b)




# n = int(sys.stdin.readline())             # qsort 변형 실패

# list = []

# def common(h):
#     for x in list:
#         if x == h: return False
#     return True

# def two_sort(a, b):
#     if len(a) == len(b) and a != b:
#         k = [a, b]
#         k.sort()
#         if k[0] == a:
#             return True
#     return False

# def quick_sort(a, left, right):
#     x = len(a[(left+right) // 2])
#     pl = left
#     pr = right

#     while pl <= pr:
#         while len(a[pl]) < x or two_sort(a[pl], a[(left+right) // 2]):
#             pl += 1
#         while len(a[pr]) > x or two_sort(a[(left+right) // 2], a[pr]):
#             pr -= 1
#         if pl <= pr:
#             if len(a[pl]) != len(a[pr]):
#                 a[pl], a[pr] = a[pr], a[pl]
#             else:
#                 z = [a[pl], a[pr]]
#                 z.sort()
#                 a[pl], a[pr] = z[0], z[1]
#             pl += 1
#             pr -= 1

#     if left<pr: quick_sort(a, left, pr)
#     if pl<right: quick_sort(a, pl, right)

# for x in range(n):
#     k = sys.stdin.readline().strip()
#     if common(k):
#         list.append(k)

# quick_sort(list, 0, len(list)-1)

# for o in list:
#     print(o)