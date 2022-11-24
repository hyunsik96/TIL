import sys

sik = sys.stdin.readline().strip()

sik = list(sik)
ans = []

for i in range(len(sik)):
    tmp = sik[i]
    if  tmp == '+':
        ans.append(tmp)
    elif tmp == '-':
        ans.append(tmp)
    else:
        if not ans or ans[-1] == '+' or ans[-1] == '-':
            ans.append(tmp)
        else:
            ans[-1] += tmp

check = 1
while check != 0:
    check = 0
    for i in range(len(ans)):
        if ans[i] == '+':
            ans[i-1] = int(ans[i-1]) + int(ans[i+1])
            ans.pop(i+1)
            ans.pop(i)
            check += 1
            break

result = int(ans[0])

if len(ans) != 1:
    for i in range(2, len(ans), 2):
        result -= int(ans[i])

print(result)