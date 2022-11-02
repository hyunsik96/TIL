import sys

sys.setrecursionlimit(100000)

# 마을 한변의 길이 n
n = int(sys.stdin.readline())

# 마을 높이정보가 담긴 2차원 배열
height = [list(map(int, sys.stdin.readline().split())) for bfde in range(n)]

# 최대 안전지역
max_area = 0

# 현재 비의 양에서 안전지역 개수
now_area = 0

# 상하좌우 안전영역 확인 재귀함수
def find_area(x, y):
    global area
    
    area[x][y] = False
    
    if x-1 >= 0:
        if area[x-1][y]: find_area(x-1,y)
    if y-1 >= 0:
        if area[x][y-1]: find_area(x,y-1)
    if x+1 < n:
        if area[x+1][y]: find_area(x+1,y)
    if y+1 < n:
        if area[x][y+1]: find_area(x,y+1)

# 비의 양을 0 ~ 100 반복
for rain in range(101):
    
    # 마을 잠김정보가 담긴 2차원 배열
    area = [[True]*n for bfde in range(n)]

    # 잠김정보 담기
    for x in range(n):
        for y in range(n):
            if height[x][y] <= rain: area[x][y] = False
    
    for x in range(n):
        for y in range(n):
            if area[x][y]:
                find_area(x, y)
                now_area += 1

    if max_area < now_area: max_area = now_area
    now_area = 0

print(max_area)