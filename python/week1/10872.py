import sys

a = int(sys.stdin.readline())
# b = 1
# if a == 0 : print(1)
# else:
#     for x in range(1, a+1):
#         b *= x
#     print(b)

def factorial(x):
    if x>1: return x*factorial(x-1)
    else: return 1

print(factorial(a))
