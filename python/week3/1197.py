import sys  # union find

input = sys.stdin.readline
v, e = map(int, input().split())
e_list = [list(map(int, input().split())) for _ in range(e)]

e_list.sort(key=lambda x: (x[2]))

parent = list(range(v + 1))

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

answer = 0

for s, e, w in e_list:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            parent[sRoot] = eRoot
        else:
            parent[eRoot] = sRoot
        answer += w

print(answer)

# import sys                        # 재귀 - 시간초과
# sys.setrecursionlimit(10000000)
# input = sys.stdin.readline
# v, e = map(int, input().split())
# e_list = [list(map(int, input().split())) for _ in range(e)]

# e_list.sort(key=lambda x: (x[2]))

# v_list = [[5,6,7]]

# max = 0
# ans = 0
# i = 0

# def is_cycle(a, b, r_list: list):
#     for x in r_list:
#         k_list = r_list[:]
#         k_list.remove(x)
#         if x[0] == a:
#             if x[1] == b: return False
#             return is_cycle(x[1], b, k_list)
#         if x[1] == a:
#             if x[0] == b: return False
#             return is_cycle(x[0], b, k_list)
#     return True

# while max < v-1:
#     now = e_list[i]
#     if is_cycle(now[0], now[1], v_list):
#         ans += now[2]
#         v_list.append(now)
#         max += 1
#     i += 1

# print(ans)


# import sys                          # 완전탐색 - 메모리초과
# from itertools import combinations

# input = sys.stdin.readline

# v, e = map(int, input().split())

# e_list = [list(map(int, input().split())) for _ in range(e)]

# com_e = list(combinations(e_list, v-1))

# find_min = sys.maxsize

# for x in com_e:
#     v_list = [0]*v
#     now = 0
#     for y in x:
#         a = y[0]
#         b = y[1]
#         v_list[a-1] += 1
#         v_list[b-1] += 1
#         now += y[2]
#     if 0 not in v_list: find_min = min(find_min, now)

# print(find_min)