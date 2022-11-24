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

print(lectures)

schedule = []
cnt = 0 # 강의실 개수
while len(lectures):
    lecture = heapq.heappop(lectures)

    if len(lectures) == 0:
        schedule.append(lecture)
        cnt += 1
        break

    tmp = []
    while lecture[1] > lectures[0][0]:
        next = heapq.heappop(lectures)

        if lecture[1] > next[1]:
            lecture = next
        else:
            heapq.heappush(tmp, next)

            if len(lectures) == 0:
                break
            else:
                continue

        if len(lectures) == 0:
            break

    cnt += 1
    schedule.append(lecture)
    if len(lectures) == 0:
        while len(tmp):
            l = heapq.heappop(tmp)
            heapq.heappush(lectures, l)

print(cnt, schedule)