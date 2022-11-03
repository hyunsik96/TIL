import sys
from itertools import permutations

n = int(sys.stdin.readline())

n_list = [int(sys.stdin.readline()) for _ in range(n)]

ans_list = [0]*n

def factorial(num):
    if num == 1 or num == 0: return 1
    else: return num * factorial(num-1)

for x in range(n):
    max_three = n_list[x] // 3

    for three in range(max_three+1):
        now = n_list[x]-3*three
        max_two = now // 2

        for two in range(max_two+1):
            one = now - 2*two
            nPr = []
            for __ in range(one): nPr.append(1)
            for __ in range(two): nPr.append(2)
            for __ in range(three): nPr.append(3)

            ans_list[x] += len(list(permutations(nPr, len(nPr)))) / (factorial(one) * factorial(two) * factorial(three))

for k in range(n):
    print(int(ans_list[k]))