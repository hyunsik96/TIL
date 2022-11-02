# a층의 탑을 b 에서 c 로 옮기기
z = []
y = 0
p = 1
q = 0 # 정답
def hanoi(a, b, c):
    if a>1: hanoi(a-1, b, 6-b-c)
    z.append(str(b)+' '+str(c))
    if a>1: hanoi(a-1,6-b-c,c)

# def hanoi2(a, b, c):                         # 시간초과
#     global y
#     if a>1: hanoi2(a-1, b, 6-b-c)
#     y += 1
#     if a>1: hanoi2(a-1,6-b-c,c)

import sys

k = int(sys.stdin.readline())


if k <=20:
    hanoi(k, 1, 3)
    print(len(z))
    for x in z:
        print(x)
else:
    for x in range(1, k+1):
        q += p
        p *= 2
    print(q)
