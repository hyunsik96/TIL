import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]            # (비용, 목적지) 가 각 리스트에 담길 것
visited = [sys.maxsize]*(n+1)               # 최대수가 각 노드에 모두 들어가 방문 여부 확인할 예정

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

def dijkstra(x):
    pq = []
    heappush(pq, (0, x))                        # 출발지역부터 0의 비용이라 생각하고 큐에 넣어주며 출발, 방문여부에도 0 삽입
    visited[x] = 0

    while pq:
        d, x = heappop(pq)                      # 큐에서 비용 가장 적은 것 팝

        if visited[x] < d:
            continue

        for nw, nx in graph[x]:
            nd = d + nw

            if visited[nx] > nd:
                heappush(pq, (nd, nx))
                visited[nx] = nd

dijkstra(start)
print(visited[end])