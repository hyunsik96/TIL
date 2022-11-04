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

def binary_search(search_list, m, start, end):
    center = (start + end) // 2

    if end - start > 1:
        if get_m(search_list, m, center):
            binary_search(search_list, m, center, end)
        else:
            binary_search(search_list, m, start, center-1)
    elif start+1 == end:
        if get_m(search_list, m, end):
            print(end)
        else: print(start)
    else: print(start)

def get_m(search_list, m, height):
    global now
    for x in search_list:
        if x > height:
            now += (x-height)
    if now >= m:
        now = 0
        return True
    else:
        now = 0
        return False

n, m = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

now = 0

quick_sort(tree, 0, n-1)

binary_search(tree, m, 0, tree[n-1])