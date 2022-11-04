import sys

def quick_sort(a, left, right):
    pl = left
    pr = right
    x = a[(left+right)//2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:					
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    if left < pr: quick_sort(a, left, pr)
    if right > pl: quick_sort(a, pl, right)

def binary_search(search_list, search_num, start, end, k):
    global ans
    if start != end:
        center = (start + end) // 2
        if search_list[center] >= search_num:
            binary_search(search_list, search_num, start, center, k)
        else:
            binary_search(search_list, search_num, center+1, end, k)
    else:
        if search_list[start] == search_num: ans_list[k] = 1


n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
find_list = list(map(int, sys.stdin.readline().split()))

# 단순 sort로 진행해도 통과
quick_sort(num_list, 0, n-1)

ans_list = [0]*m


for x in range(m):
    binary_search(num_list, find_list[x], 0, n-1, x)

for y in ans_list:
    print(y)