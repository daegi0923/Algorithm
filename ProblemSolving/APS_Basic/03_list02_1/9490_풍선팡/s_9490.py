import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    max_pang = 0
    for i in range(N):
        for j in range(M):
            pang = -mat[i][j]
            cnt = mat[i][j]
            for x in range(i-cnt, cnt+i+1):
                if 0 <= x < N:
                    pang = pang + mat[x][j]
            for y in range(-cnt+j, cnt+j+1):
                if 0 <= y < M:
                    pang = pang + mat[i][y]
                    if pang > max_pang:
                        max_pang = pang
    print(f'#{t+1} {max_pang}')
