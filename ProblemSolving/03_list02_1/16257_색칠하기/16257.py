import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    mat = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                mat[r][c] =  mat[r][c] + color

    area = 0
    for r, col_num in enumerate(mat):
        for c, color in enumerate(col_num):
            if color == 3:
                area = area + 1
    print(f'#{t+1} {area}')