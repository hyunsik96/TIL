a = [1, 2, 3, 4, 4]
print(a[1])
a[2] = 100
a.append(4)
a.extend([5, 6, 7])
a.remove(4)
print(a)

b = (1, 2, 3) # 튜플은 데이터 변경 불가
c = 1, 2, 3
print(b[1])
print(c[1])

d = {1, 2, 3, 2} # 세트는 인덱스 개념 없고 중복 불가능
print(d)

e = {'a': 1, 'b': 2, 'c': 3}
print(e['b'])

a = [int(x) for x in input().split()]  # 가 반복돌며 리스트에 들어감

import sys  
a = list(map(int, input().split()))

f = [1, 3, 2]
f.sort(reverse=True)