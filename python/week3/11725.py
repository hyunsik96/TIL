import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())
ans = [0]*(n+1)

tree = [{0} for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].add(b)
    tree[b].add(a)

def dfs(num):
    for k in list(tree[num])[1:]:
        if ans[k] == 0:
            ans[k] = num
            dfs(k)
dfs(1)
print(*ans[2:], sep='\n')




# import sys                      # 시간초과
# from collections import deque
# input = sys.stdin.readline

# n = int(input())

# level = [0]*(n+1)
# level[1] = 1
# ans = [0]*(n+1)
# put_list = deque([list(map(int, input().split())) for _ in range(n-1)])


# while put_list:
#     now = put_list.popleft()
#     if level[now[0]] != 0 and level[now[1]] == 0:
#         level[now[1]] = level[now[0]] + 1
#         ans[now[1]] = now[0]
#     elif level[now[1]] != 0 and level[now[0]] == 0:
#         level[now[0]] = level[now[1]] + 1
#         ans[now[0]] = now[1]
#     elif level[now[1]] == 0 and level[now[0]] == 0:
#         put_list.append(now)

# print(*ans[2:], sep='\n')