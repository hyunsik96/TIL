import sys

n = int(sys.stdin.readline())
n_list = [sys.stdin.readline().replace('\n', '') for _ in range(n)]



ans2 = f'({n_list[0][0]}{n_list[0][1]}{n_list[1][0]}{n_list[1][1]})'

ans4 = ''
a = 0
b = 0
ans4 += f'({n_list[a][b]}{n_list[a][b+1]}{n_list[a+1][b]}{n_list[a+1][b+1]})'
b += 2
ans4 += f'({n_list[a][b]}{n_list[a][b+1]}{n_list[a+1][b]}{n_list[a+1][b+1]})'
b -= 2
a += 2
ans4 += f'({n_list[a][b]}{n_list[a][b+1]}{n_list[a+1][b]}{n_list[a+1][b+1]})'
b += 2
ans4 += f'({n_list[a][b]}{n_list[a][b+1]}{n_list[a+1][b]}{n_list[a+1][b+1]})'
ans41 = f'({ans4})'

ans42 = ''


def wb(xa, xb, ya, yb, d):
    for i in range(xa, xb+1):
        for m in range(ya, yb+1):
            if '0' == n_list[i][m]: ''