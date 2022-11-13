import sys
sub_string = list(sys.stdin.readline().rstrip())
boomer = list(sys.stdin.readline().rstrip())
length = len(boomer)    # 폭탄 길이 정의

stack = []

for i in sub_string:
    stack.append(i)
    # 스택의 뒷 N개 폭탄과 일치 조건
    if stack[-length:] == boomer:
        for _ in range(length):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))