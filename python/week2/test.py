import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = [list(map(int, list(input().rstrip()))) for _ in range(N)]

def is_full_with(a: list):
    n = len(a)
    num = a[0][0]
    for i in range(n):
        for j in range(n):
            if a[i][j] != num:
                return -1
    return num

def sol(a: list):
    na = len(a) // 2
    
    if is_full_with(a) == 0:
        print(0, end='')
        return

    elif is_full_with(a) == 1:
        print(1, end ='')
        return   

    else:
        print ('(', end='')
        sol([i[:na] for i in a[:na]])
        sol([i[na:] for i in a[:na]])
        sol([i[:na] for i in a[na:]])
        sol([i[na:] for i in a[na:]])
        print(')', end='')

sol(A)