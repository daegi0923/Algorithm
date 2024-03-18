import sys


sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N = int(input())
    mat = [[0]*N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = j = d =0
    for num in range(1, N**2+1):
        mat[i][j] = num
        # print(i, j, num, "  i, j")
        if d%2 == 0 and (j+1-d < 0 or j+1-d > N-1 or mat[i][j+1-d] != 0):
            d = (d + 1)%4
        elif d%2 == 1 and (i+2-d < 0 or i+2-d > N-1 or mat[i+2-d][j] != 0):
            d = (d + 1)%4
        i = i + di[d]
        j = j + dj[d]
    print(f'#{t+1}')
    [print(*r) for r in mat]