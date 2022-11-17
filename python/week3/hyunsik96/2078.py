import sys                                                                                        # 아래서부터 올라가기

a, b = map(int, sys.stdin.readline().split())
left = 0
right = 0

while a != 1 or b != 1:
    if a > b:
        left += 1
        a = a-b
    else:
        right += 1
        b = b-a

print(f'{left} {right}')


# import sys                                                                                        # 위부터 내려가기 - 메모리초과
# from collections import deque

# a, b = map(int, sys.stdin.readline().split())

# queue = deque([[1, 1, 0, 0]])

# while queue:
#     now = queue.popleft()

#     if now[0] == a and now[1] == b:
#         print(f'{now[2]} {now[3]}')
#         break

#     if now[0]+now[1] <= a:
#         queue.append([now[0]+now[1], now[1], now[2]+1, now[3]])
#     if now[0]+now[1] <= b:
#         queue.append([now[0], now[0]+now[1], now[2], now[3]+1])