import sys

k = int(sys.stdin.readline())

k_list = [int(sys.stdin.readline()) for _ in range(k)]

ans_list = []

for x in k_list:
    if x != 0:
        ans_list.append(x)
    else:
        ans_list.pop()

print(sum(ans_list))