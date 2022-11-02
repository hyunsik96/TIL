import sys

a = int(sys.stdin.readline())

b = 0 # 정답담기
c = 0 # 등차 확인 일시적

if a < 100: b = a
else:
    b += 99
    for x in range(100, a+1):
        if int(str(x)[1]) - int(str(x)[0]) == int(str(x)[2]) - int(str(x)[1]):
            b += 1
print(b)