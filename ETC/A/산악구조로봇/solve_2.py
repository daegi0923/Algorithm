import sys

sys.stdin = open('input.txt')

from collections import deque
def cal_cost(i, j):
    height = matrix[i][j]
    paths = []
    if 0<i<N:
        paths.append((i-1, j))
    if 0<j<N:
        paths.append((i, j-1))
    local_min = float('inf')
    min_path_i, min_path_j = paths[0]
    for path in paths:
        prev_i, prev_j = path
        path_h = matrix[prev_i][prev_j]
        if path_h < height:
            cost = (height - path_h)*2
        elif height < path_h:
            cost = 0
        elif path_h == height:
            cost = 1

        if cost+cost_mat[prev_i][prev_j] < local_min:
            local_min = cost + cost_mat[prev_i][prev_j]
    if (i, j) in tunnels:
        if tunnels[(i, j)]['cost'] < local_min:
            min_path_i, min_path_j = tunnels[(i, j)]['end']
            local_min = tunnels[(i, j)]['cost'] + cost_mat[min_path_i][min_path_j]
    return local_min

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    cost_mat = [[0]*N for _ in range(N)]
    tunnels  = {}
    min_cost = float('inf')
    for _ in range(M):
        ai, aj, bi, bj, c = map(int,input().split())
        if ai < bi:
            tunnels[(bi-1, bj-1)] = {'end': (ai-1, aj-1), 'cost': c}
        elif bi < ai:
            tunnels[(ai-1, aj-1)] = {'end': (bi-1, bj-1), 'cost': c}
        elif ai == bi:
            if aj < bj:
                tunnels[(bi-1, bj-1)] = {'end': (ai-1, aj-1), 'cost': c}
            elif bj < aj:
                tunnels[(bi-1, bj-1)] = {'end': (ai-1, aj-1), 'cost': c}
    # print(tunnels)
    # print(matrix)
    for i in range(N):
        for j in range(N):
            if (i, j) == (0, 0):
                continue
            cost_mat[i][j] = cost_mat[i][j] + cal_cost(i, j)
#     [print(*row) for row in cost_mat]

    print(f'#{t} {cost_mat[N-1][N-1]}')
