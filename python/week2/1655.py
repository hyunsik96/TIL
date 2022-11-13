import sys
import heapq

n = int(sys.stdin.readline())

l_heap = []
r_heap = []
heapq.heappush(l_heap, -1*int(sys.stdin.readline()))
print(-1*l_heap[0])

for x in range(n-1):
    if (x)%2 == 0:  # 홀수에서 한개 추가하여 짝수되는 과정
        k = int(sys.stdin.readline())
        now = heapq.heappop(l_heap)*-1
        if now <= k:
            heapq.heappush(r_heap, k)
            heapq.heappush(l_heap, -1*now)
            print(now)
        else:
            heapq.heappush(l_heap, -1*k)
            heapq.heappush(r_heap, now)
            tmp = heapq.heappop(l_heap)*-1
            print(tmp)
            heapq.heappush(l_heap, -1*tmp)
        

    else:           # 짝수에서 한개 추가하여 홀수되는 과정
        k = int(sys.stdin.readline())
        now = heapq.heappop(l_heap)*-1
        if now >= k:
            heapq.heappush(l_heap, -1*k)
            heapq.heappush(l_heap, -1*now)
            print(now)
        else:
            r_now = heapq.heappop(r_heap)
            if r_now <= k:
                heapq.heappush(l_heap, r_now*-1)
                heapq.heappush(r_heap, k)
                heapq.heappush(l_heap, -1*now)
            else:
                heapq.heappush(l_heap, k*-1)
                heapq.heappush(r_heap, r_now)
                heapq.heappush(l_heap, -1*now)
            tmp = heapq.heappop(l_heap)*-1
            print(tmp)
            heapq.heappush(l_heap, -1*tmp)




# import sys            # center 좌표 이동시켜봤지만 실패
# import bisect
# n = int(sys.stdin.readline())
# k_list = [int(sys.stdin.readline())]
# print(k_list[0])
# center = 0
# for x in range(n-1):
#     if (x)%2 == 0:  # 홀수에서 한개 추가하여 짝수되는 과정
#         bisect.insort(k_list, int(sys.stdin.readline()))
#         print(k_list[center])
#     else:           # 짝수에서 한개 추가하여 홀수되는 과정
#         k = int(sys.stdin.readline())
#         center += 1
#         bisect.insort(k_list, k)
#         print(k_list[center])



# import bisect           # 이분탐색삽입 활용하였지만 시간초과
# import sys
# n = int(sys.stdin.readline())
# k_list = []
# for x in range(n):
#     bisect.insort(k_list, int(sys.stdin.readline()))
#     k = int((x+1)//2)
#     if (x+1)%2 == 0: print(min(k_list[k-1], k_list[k]))
#     else: print(k_list[k])