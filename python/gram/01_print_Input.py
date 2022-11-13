print('ㅎㅇ')
a = input('입력하세요 : ')
print(a)

print('ㅎㅇ', end='')
b = input()
print(b)

print(f'안녕 {a}는 {b}이냐?')

import sys

sys.stdin.readline() # 이거로 데이터 받는게 처리속도상 input 보다 빠름

input = sys.stdin.readline

a = input().rstrip()    # 가장 오른쪽 하나 날림 (\n 도 한번에 날려줌)

