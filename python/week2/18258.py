import sys
from collections import deque

n = int(sys.stdin.readline())
m_list = [sys.stdin.readline().replace('\n', '') for _ in range(n)]

s_list = deque([])
ans_list = []

for m in m_list:
    if m.split()[0] == 'push':
        s_list.append(m.split()[1])
    elif m.split()[0] == 'pop':
        if len(s_list) != 0:
            ans_list.append(s_list.popleft())
        else: ans_list.append(-1)
    elif m.split()[0] == 'size':
        ans_list.append(len(s_list))
    elif m.split()[0] == 'empty':
        if len(s_list) == 0: ans_list.append(1)
        else: ans_list.append(0)
    elif m.split()[0] == 'front':
        if len(s_list) == 0: ans_list.append(-1)
        else:
            ans_list.append(s_list[0])
    elif m.split()[0] == 'back':
        if len(s_list) == 0: ans_list.append(-1)
        else:
            ans_list.append(s_list[-1])

for x in ans_list:
    print(x)