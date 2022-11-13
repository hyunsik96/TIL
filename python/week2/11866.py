import sys

n, k = map(int, sys.stdin.readline().split())

n_list = [int(i) for i in range(1, n+1)]
ans_list = []

a = k-1
ans_list.append(n_list.pop(a))
a = a-1

while n_list:
    a = a+k
    if a >= len(n_list):
        a = a % len(n_list)
        ans_list.append(n_list.pop(a))
        a = a-1
    else:
        ans_list.append(n_list.pop(a))
        a = a-1

print('<', end='')
for x in range(0, n-1):
    print(ans_list[x], end=', ')
print(ans_list[-1], end='>')