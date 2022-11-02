import sys

n = int(sys.stdin.readline())

# height층의 탑을 a 에서 b 로 옮기기
trace_plate = []
mul = 1
ans = 0 # 정답
def hanoi(height, a, b):
    if height>1: hanoi(height-1, a, 6-a-b)
    trace_plate.append(str(a)+' '+str(b))
    if height>1: hanoi(height-1,6-a-b,b)

if n <=20:
    hanoi(n, 1, 3)
    print(len(trace_plate))
    for x in trace_plate:
        print(x)
else:
    for x in range(1, n+1):
        ans += mul
        mul *= 2
    print(ans)