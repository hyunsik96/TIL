import sys
input = sys.stdin.readline
import heapq

N = int(input())

def swap(lecture: list):
    lecture[0], lecture[1] = lecture[1], lecture[0]
    lecture[1], lecture[2] = lecture[2], lecture[1]

    return tuple(lecture)

lectures = [list(map(int, input().split())) for _ in range(N)]
lectures = list(map(swap, lectures))
lectures.sort()
heapq.heapify(lectures)


while lectures:
    print(heapq.heappop(lectures))