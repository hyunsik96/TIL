import sys

m, n, l = map(int, sys.stdin.readline().split())

m_list = list(map(int, sys.stdin.readline().split()))

m_list.sort()

n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 0

for x in n_list:
    pl = 0
    pr = m-1
    now_m = 0
    while pl <= pr:
        if pl + 1 < pr:
            center = (pl + pr)//2
            if m_list[center] > x[0]:
                pr = center
            elif m_list[center] < x[0]:
                pl = center
            else:
                now_m = m_list[center]
                break
        else:
            if (x[0] - m_list[pl])**2 <= (x[0] - m_list[pr])**2: now_m = m_list[pl]
            else: now_m = m_list[pr]
            break

    if now_m >= x[0]:
        if now_m - x[0] + x[1] <= l: ans += 1
    else:
        if x[0] - now_m + x[1] <= l: ans += 1

print(ans)