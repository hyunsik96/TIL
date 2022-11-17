import sys
sys.setrecursionlimit(100000)
f_list = []
while True:
    try:
        f_list.append(int(sys.stdin.readline()))
    except:
        break


def cut(ran_list):
    n_pop = ran_list.pop(0)
    list_size = len(ran_list)
    test_num = list_size

    for i in range(0, list_size):
        if n_pop < ran_list[i]:
            test_num = i
            break
    
    if ran_list[0:test_num]: cut(ran_list[0:test_num])
    if ran_list[test_num:list_size]: cut(ran_list[test_num:list_size])
    print(n_pop)

cut(f_list)