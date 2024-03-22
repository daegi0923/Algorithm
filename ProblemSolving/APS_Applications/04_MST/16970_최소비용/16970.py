import sys
sys.stdin = open('input.txt')

import heapq


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    cost_mat = [[float('inf')] * N for _ in range(N)]
    cost_mat[0][0] = 0
    hq = [[0, 0, 0]]
    while hq:
        c_cost, ci, cj = heapq.heappop(hq)
        # print(ci, cj)
        # print(cost_mat)
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            if ni == N or nj == N:
                print(ni, nj)
            if 0 <= ni < N and 0 <= nj < N:
                nc = 1
                if mat[ci][cj] < mat[ni][nj]:
                    nc = nc + mat[ni][nj] - mat[ci][cj]
                if cost_mat[ni][nj] > c_cost + nc:
                    cost_mat[ni][nj] = c_cost + nc
                    heapq.heappush(hq, [c_cost+nc, ni, nj])
    # print(cost_mat)
    print(f'#{t} {cost_mat[N-1][N-1]}')
