import sys
from collections import deque
from heapq import heappop, heappush


def bfs():
    # 번호가 낮은 바이러스가 순서대로 자리 차지함
    while q:
        # num, X_Y_day = heappop(heap)
        # num, X_Y_day = q.popleft()
        tmp = q.popleft()
        num, X_Y_day = tmp
        for i in range(4):
            nx = X_Y_day[0] + dx[i]
            ny = X_Y_day[1] + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if S <= X_Y_day[-1] and X == nx + 1 and Y == ny + 1:
                    return arr[nx][ny]
                # 아직 바이러스가 자리 차지를 하지 않았다면
                if arr[nx][ny] == 0:
                    arr[nx][ny] = num
                    # heappush(heap, (arr[nx][ny], (nx, ny, (X_Y_day[-1] + 1))))
                    q.append((arr[nx][ny], (nx, ny, (X_Y_day[-1] + 1))))


input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

days = 0
# heap = []
lst = []
q = deque()
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            lst.append((arr[i][j], (i, j, days)))
            # heappush(heap, (arr[i][j], (i, j, days)))
            # q.append((arr[i][j], (i, j, days)))

lst.sort()
for virus_num, position_x_y in lst:
    q.append((virus_num, position_x_y))

S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())