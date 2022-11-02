import sys

n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for bfde in range(n)]
b = [0]*n
min_ = sys.maxsize

def dfs(d, s, c):
    global min_
    if d == n-1 and a[s][0] != 0:
        min_ = min(min_, c+a[s][0])
        return
    for i in range(n):
        if not b[i] and a[s][i] != 0:
            b[i] = 1
            dfs(d+1, i, c+a[s][i])
            b[i] = 0
b[0] = 1
dfs(0, 0, 0)
print(min_)


# import sys                                                        # 재귀2
# N = int(input())
# min_value = 1000000* (N)
# travel = []
# for _ in range(N):
#     travel.append(list(map(int,input().split(' '))))

# def dfs(startNode, nextNode, value, visited):
#     global min_value

# 	# 다 순회하지 않아도 min_value를 초과하면 다 순회할 필요가 없다.
#     if value + travel[nextNode][startNode] > min_value:
#         return False

# 	# 모든 노드를 순회한 경우
#     if len(visited) == N:
#     	# 마지막 노드에서 제일 처음으로 방문한 노드로 오는 방법이 있는지
#         if travel[nextNode][startNode] != 0:
#             min_value = value + travel[nextNode][startNode]
#             return True
#         return False

#     for i in range(N):
#         # 갈 수 있는 노드인지 + 이미 방문한 노드는 아닌지
#         if travel[nextNode][i] != 0 and i not in visited:
#             visited.append(i)
#             dfs(startNode, i, value+travel[nextNode][i], visited)
#             visited.pop()

# # i는 시작하는 node
# # [i]를 하는 이유는 마지막으로 돌아올 노드를 넣어줌
# # 기본적으로 backtracking
# result = 0
# for i in range(N):
#     dfs(i, i, 0, [i])
        
# print(min_value)



# nPr = list(itertools.permutations(b, n))      # 순열 활용, 시간 및 메모리 초과

# for y in range(len(nPr)):
#     k = 0
#     m = 0
#     c = nPr[y]
#     for z in range(n-1):
#         if a[c[z]][c[z+1]] != 0:
#             k += a[c[z]][c[z+1]]
#         else: m += 1
#     if a[c[n-1]][c[0]] != 0:
#             k += a[c[n-1]][c[0]]
#     else: m += 1
#     if y == 0: min_ = k
#     if m == 0:
#         min_ = min(min_, k)
# print(min_)