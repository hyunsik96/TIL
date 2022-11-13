import sys

n = int(sys.stdin.readline())
p_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans0 = 0
ans1 = 0

def cut_paper(xa, xb, ya, yb, d):
    global ans0, ans1
    if get_tf(xa, xb, ya, yb, 0): ans0 += 1
    elif get_tf(xa, xb, ya, yb, 1): ans1 += 1
    else:
        cut_paper(xa, xb-d/2, ya, yb-d/2, d/2)
        cut_paper(xa+d/2, xb, ya, yb-d/2, d/2)
        cut_paper(xa, xb-d/2, ya+d/2, yb, d/2)
        cut_paper(xa+d/2, xb, ya+d/2, yb, d/2)

def get_tf(xa, xb, ya, yb, ans):
    for x in range(int(xa), int(xb+1)):
        for y in range(int(ya), int(yb+1)):
            if p_list[x][y] != ans:
                return False
    return True

cut_paper(0, n-1, 0, n-1, n)

print(ans0)
print(ans1)