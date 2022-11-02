a = ['abc', 'aaa']


def two_sort(a, b):
    if len(a) == len(b):
        k = [a, b]
        k.sort()
        if k[0] == a: return True
    return False

if two_sort('abc', 'aaa'):
    print('True')
else: print('False')