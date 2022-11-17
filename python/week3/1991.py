import sys

input = sys.stdin.readline

n = int(input())

tree = [input().rstrip().split() for _ in range(n)]

def f_trip(root_list):
    print(root_list[0], end='')
    if root_list[1] != '.':
        for x in tree:
            if x[0] == root_list[1]:
                f_trip(x)
                break
    if root_list[2] != '.':
        for x in tree:
            if x[0] == root_list[2]:
                f_trip(x)
                break

def c_trip(root_list):
    if root_list[1] != '.':
        for x in tree:
            if x[0] == root_list[1]:
                c_trip(x)
                break
    print(root_list[0], end='')
    if root_list[2] != '.':
        for x in tree:
            if x[0] == root_list[2]:
                c_trip(x)
                break

def b_trip(root_list):
    if root_list[1] != '.':
        for x in tree:
            if x[0] == root_list[1]:
                b_trip(x)
                break
    if root_list[2] != '.':
        for x in tree:
            if x[0] == root_list[2]:
                b_trip(x)
                break
    print(root_list[0], end='')

f_trip(tree[0])
print()
c_trip(tree[0])
print()
b_trip(tree[0])