import sys

sys.stdin = open('input.txt')

from collections import deque
import heapq



N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
MAP_t = list(zip(*MAP[::-1]))
# print(MAP_t)
ans = float('inf')
di = [0, 0]
dj = [1, -1]
start = [(row_num,row.index(2)) for row_num, row in enumerate(MAP) if 2 in row][0]
end = [(row_num,row.index(3)) for row_num, row in enumerate(MAP) if 3 in row][0]
cost_mat = [[float('inf')]*M for _ in range(N)]
si, sj = start
ei, ej = end
pq = [[0, si, sj]]
cost_mat[si][sj] = 0
while pq:

    cc, ci, cj = heapq.heappop(pq)
    # if ci == ei and cj == ej:
    #     break
    nexts = []
    for d in range(2):
        nj = cj+dj[d]
        if 0<=nj<M and MAP[ci][nj]:
            if cost_mat[ci][nj] > cost_mat[ci][cj]:
                heapq.heappush(pq,[cost_mat[ci][cj], ci, nj])
                cost_mat[ci][nj] = cost_mat[ci][cj]

    for d in range(N):
        ni = ci + d
        if 0<= ni < N and MAP[ni][cj] and cost_mat[ni][cj] > max(cc,d):
            heapq.heappush(pq, [max(cc,d), ni, cj])
            cost_mat[ni][cj] = max(cc,d)
            break
    for d in range(N):
        ni = ci - d
        if 0<= ni < N and MAP[ni][cj] and cost_mat[ni][cj] > max(cc,d):
            heapq.heappush(pq, [max(d, cc), ni, cj])
            cost_mat[ni][cj] = max(d, cc)
            break
# [print(*row) for row in cost_mat]
print(cost_mat[ei][ej])


