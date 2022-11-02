a = int(input()) # 테스트 시행 횟수
b = [] # 시행이 담길 리스트
c = 0 # O 가 몇번째 연속되고 있는지 확인
d = 0 # 한행 점수 합산용
e = [] # 정답 저장용
for x in range(a):
    b.append(input())

for y in range(a):
    for z in range(len(b[y])):
        if b[y][z] == 'O':
            c += 1
            d += c
        else: c = 0
    e.append(d)
    d = 0
    c = 0
for q in e:
    print(q)