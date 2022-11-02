a = int(input())
b = int(input())

print(a*(b%10))
print(int(a*(b%100-b%10)/10))
print(int(a*(int(b/100))))
print(int(a*(b%10)+a*(b%100-b%10)+a*(int(b/100))*100))