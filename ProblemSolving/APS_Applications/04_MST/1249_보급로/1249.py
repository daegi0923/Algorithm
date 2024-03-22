import sys

sys.stdin = open('input.txt')

import heapq


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [input() for _ in range(N)]
    hq = [[0, 0, 0]]
    cost_mat = [[float('inf')]*N for _ in range(N)]
    cost_mat[0][0] = 0
    while hq:
        cc, ci, cj = heapq.heappop(hq)
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                nc = int(mat[ni][nj])
                if cc + nc < cost_mat[ni][nj]:
                    heapq.heappush(hq, [nc+cc, ni, nj])
                    cost_mat[ni][nj] = cc + nc
    # print(cost_mat)
    print(f'#{t} {cost_mat[N-1][N-1]}')