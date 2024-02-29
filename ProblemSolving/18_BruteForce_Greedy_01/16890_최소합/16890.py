import sys
sys.stdin = open('input.txt')
from collections import deque
T = int(input())
di = [1, 0]
dj = [0, 1]

for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    cost_mat = [[float('inf')] * N for _ in range(N)]
    q = deque()
    q.append((0, 0))
    cost_mat[0][0] = matrix[0][0]
    ans = 0
    while q:
        ci, cj = q.popleft()
        for d in range(2):
            ni = ci + di[d]
            nj = cj + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if cost_mat[ni][nj] > cost_mat[ci][cj] + matrix[ni][nj]:
                    cost_mat[ni][nj] = cost_mat[ci][cj] + matrix[ni][nj]
                    q.append((ni ,nj))
    print(f'#{t} {cost_mat[N-1][N-1]}')
