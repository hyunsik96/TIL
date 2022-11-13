import sys

a = sys.stdin.readline().replace('\n', '')
bomb = sys.stdin.readline().replace('\n', '')

while bomb in a:
    a = a.replace(bomb, '')

if len(a) == 0:
    print('FRULA')
else:
    print(a)