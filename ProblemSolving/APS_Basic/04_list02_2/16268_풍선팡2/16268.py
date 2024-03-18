import sys


sys.stdin = open('input.txt')
T = int(input())

for t in range(T):
    N, M = map(int,input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    max_pang = 0
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    for i in range(N):
        for j in range(M):
            curr = mat[i][j]
            for d in range(4):
                if 0<= i + di[d] < N and 0<=j+dj[d] < M:
                    curr = curr + mat[i + di[d]][j+dj[d]]
            if curr > max_pang:
                max_pang = curr
    print(f'#{t+1} {max_pang}')