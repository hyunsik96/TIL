import sys
from itertools import combinations

input_value = list(map(int, sys.stdin.readline().split()))
num_list = list(map(int, sys.stdin.readline().split()))
ans = 0

for x in range(1, input_value[0]+1):
    for y in list(combinations(num_list, x)):
        if sum(y) == input_value[1]: ans += 1

print(ans)