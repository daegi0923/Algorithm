import sys


sys.stdin = open('input.txt')

for t in range(10):
    N = int(input())
    mat = [input() for _ in range(8)]
    ans = 0
    for i in range(8):
        for j in range(8-N+1):
            # 가로
            axis_x = mat[i][j:j+N]
            if axis_x == axis_x[::-1]:
                ans = ans + 1
    for i in range(8-N+1):
        for j in range(8):
            #세로
            axis_y = ''.join([mat[i + x][j] for x in range(N)])
            if axis_y == axis_y[::-1]:
                ans = ans + 1
    print(f'#{t+1} {ans}')