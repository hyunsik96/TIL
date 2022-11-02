a = int(input())
list = []
for x in range(a):
    b, c = input().split()
    list.append(int(b)+int(c))

for y in list:
    print(y)
