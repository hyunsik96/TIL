a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c) - a
d = int(d) - b
if(a<=b and a<=c and a<=d): print(a)
elif(b<=a and b<=c and b<=d): print(b)
elif(c<=a and c<=b and c<=d): print(c)
else: print(d)