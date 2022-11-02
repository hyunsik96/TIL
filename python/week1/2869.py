a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = 0  
e = 0 # 정답
# while True:
#     e += 1
#     d += a
#     if d >= c:
#         print(e)
#         break
#     d -= b               # 시간초과

import math
e = math.ceil((c-b)/(a-b))

print(e)