import sys                  # dfs -> 체크를 하며 연결지점을 탐색. 
                            # 체크를 어떻게 할지와 연결지점을 어떻게 탐색할지 고민
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

k = int(input())

def dfs(start, group):
    check[start] = group

    for i in e_list[start]:
        if not check[i]:
            a = dfs(i, -group)
            if not a:
                return False
        elif check[i] == check[start]:
                return False
    return True


for i in range(k):

    v, e = map(int, input().split())
    e_list = [[] for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        e_list[a].append(b)
        e_list[b].append(a)

    check = [False]*(v+1)

    for i in range(1, v+1):
        if not check[i]:
            result = dfs(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')
    
    






# import sys                            # 시간초과
# import copy
# sys.setrecursionlimit(100000000)
# input = sys.stdin.readline

# k = int(input())
# ans = ['']*k

# def dfs(num):
#     check[num] = True
#     if no_edge(): return True
#     else:
#         tem_list = list(range(1, v+1))
#         tem_list.remove(num)
#         for x in e_list[num]:
#             tem_list.remove(x)
#         for y in tem_list:
#             if not check[y]:
#                 if dfs(y): return True
#                 else: check[y] = False
#     return False


# def no_edge():
#     test = copy.deepcopy(e_list)
#     for i in range(1, v+1):
#         if check[i]:
#             while test[i]:
#                 tem = test[i].pop()
#                 try: test[tem].remove(i)
#                 except: None
#     if test == [[]]*(v+1): return True
#     else: return False
            

# for i in range(k):

#     v, e = map(int, input().split())
#     e_list = [[] for _ in range(v+1)]

#     for _ in range(e):
#         a, b = map(int, input().split())
#         e_list[a].append(b)
#         e_list[b].append(a)

#     check = [False]*(v+1)
    
#     if dfs(1):
#         ans[i] = 'YES'
#     else: ans[i] = 'NO'

# print(*ans, sep='\n')






# import sys                    # 순환이 없는지만 확인

# input = sys.stdin.readline

# k = int(input())
# ans = ['']*k

# for i in range(k):

#     v, e = map(int, input().split())
#     e_list = [[] for _ in range(v+1)]

#     for _ in range(e):
#         a, b = map(int, input().split())
#         e_list[a].append(b)
#         e_list[b].append(a)

#     if e >= v: ans[i] = 'NO'
#     else:
#         cycle_check = 1
#         while cycle_check != 0:
#             cycle_check = 0
#             for l in range(1, v+1):
#                 if len(e_list[l]) == 1:
#                     cycle_check += 1
#                     tem = e_list[l][0]
#                     try:
#                         e_list[l].remove(tem)
#                         e_list[tem].remove(l)
#                     except: None
        
#         if e_list == [[]]*(v+1): ans[i] = 'YES'
#         else: ans[i] = 'NO'

# print(*ans, sep='\n')
