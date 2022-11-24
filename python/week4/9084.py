import sys
input = sys.stdin.readline

t = int(input())

# 테스트 케이스 반복
for _ in range(t):

    # 동전 가지수, 동전종류(오름차순), 만들 돈
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())

    # 0 원 ~ m 원 을 만드는 가짓수
    tmp_list = [0]*(m+1)
    tmp_list[0] = 1

    # 중복을 막기위해 한 종류씩 채우고 다음 종류 채울 때 한칸씩 탐색하며 더하기
    for c in coin:
        for d in range(c, m+1):
            tmp_list[d] += tmp_list[d-c]

    print(tmp_list[m])

    # # 중복으로 실패
    # # 동전 종류마다 그 금액을 만드는 가짓수를 1로 설정
    # for i in range(n):
    #     tmp_list[coin[i]] = 1

    # # 0 원 부터 m 원 까지 dp로 가짓수 찾기
    # for x in range(m+1):

    #     # 현재 x 원 만들 때 x원 이하의 동전
    #     tmp_coin = []

    #     for y in range(n):
    #         if x >= coin[y]: tmp_coin.append(y)
    #         else: break

    #     for z in tmp_coin:
    #         if x-coin[z] not in tmp_coin:
    #             tmp_list[x] += tmp_list[x-coin[z]]

    # print(tmp_list[m])