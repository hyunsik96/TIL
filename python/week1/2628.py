import sys

a, b = map(int, sys.stdin.readline().split()) # 가로, 세로

c = int(sys.stdin.readline()) # 자르는 횟수

d = [0, a] # 가로 배열 [0, 10, 1, 2, 3] 근접한 두 값중 차이가 가장 큰 값 (순서대로 정렬부터 시키고)
e = [0, b] # 세로 배열

for x in range(c):
    f, g = map(int, sys.stdin.readline().split())
    if f == 0: e.append(g)
    else: d.append(g)

d.sort()
e.sort()
h = 0
i = 0

for y in range(1, len(d)):
    if d[y] - d[y-1] > h: h = d[y] - d[y-1]

for z in range(1, len(e)):
    if e[z] - e[z-1] > i: i = e[z] - e[z-1]

print(h*i)
