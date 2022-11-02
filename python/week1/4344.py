a = int(input()) # 몇 줄 받을지 = a
b = [] # 한줄씩 받을 때 잠시 넣어둘 리스트
c = [] # 결과 저장해둘 리스트
d = 0 # 평균 구할 때 잠시 더해두는 곳
e = 0 # 평균보다 몇명이 넘나 확인용

for x in range(a): # 몇 줄 받을지 반복
    b = input().split() # 한 줄당 받아서 b에 임시 저장
    for y in range(int(b[0])): # b 에 반복돌림
        d += int(b[y+1])
    d = (d / int(b[0])) # 이게 평균

    for z in range(int(b[0])):
        if int(b[z+1]) > d: e+=1
    c.append(round(e / int(b[0]) * 100, 3))
    e = 0
    d = 0

for q in c:
    print("{:.3f}%".format(q))