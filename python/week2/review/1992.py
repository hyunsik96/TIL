import sys
N = int(sys.stdin.readline())
n_list = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
result = []

# 픽셀 읽을 함수 정의
def read_pixel(x, y, N):
  pixel = n_list[x][y]  # 픽셀 값 정의
  for i in range(x, x+N):
    for j in range(y, y+N):
      if pixel != n_list[i][j]: # 픽셀 값이 달라지는 경우 분기 발생
        # 각 좌표에 따른 분기 발생 시 '()' 추가
        result.append('(')
        read_pixel(x, y, N//2)
        read_pixel(x, y+N//2, N//2)
        read_pixel(x+N//2, y, N//2)
        read_pixel(x+N//2, y+N//2, N//2)
        result.append(')')
        return
  if pixel == 0 :
    # print 시 .join()을 위해 str형으로 append
    result.append('0')
  else :
    result.append('1')

# 함수 호출
read_pixel(0, 0, N)
# 리스트 요소 한 줄 출력
print(''.join(result))