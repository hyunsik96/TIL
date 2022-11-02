a = int(input())
b = '' # 입력받는 행 저장용
c = '' # 22
d = '' # 정답 저장용
e = [] # 정답 저장하는 리스트
for x in range(a):
    b, c = input().split()
    for y in range(len(c)):
        for z in range(int(b)):
            d += c[y]
    e.append(d)
    d = ''
for q in e:
    print(q)