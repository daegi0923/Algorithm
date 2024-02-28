import sys


sys.stdin = open('input.txt')

from queue import PriorityQueue

import heapq


def cal_cost(start_i, start_j, end_i, end_j):
    cost = 0
    if (start_i, start_j) in tunnels:
        if tunnels[(start_i, start_j)]['end'] == (end_i, end_j):
            return tunnels[(start_i, start_j)]['cost']
    s_height = matrix[start_i][start_j]
    e_height = matrix[end_i][end_j]
    if s_height < e_height:
        cost = (e_height - s_height)*2
    elif e_height < s_height:
        cost = 0
    elif s_height == e_height:
        cost = 1
    return cost

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def getEdge(i, j):
    next_nodes = []
    for d in range(4):
        next_i = i + di[d]
        next_j = j + dj[d]
        if 0 <= next_i < N+1 and 0 <= next_j < N+1:
            next_nodes.append((next_i, next_j))
    if (i, j) in tunnels:
        next_nodes.append(tunnels[(i, j)]['end'])
    return next_nodes


T = int(input())
for t in range(1, T+1):
    N,M = map(int,input().split()) # N : 맵 크기 M : 터널 개수
    matrix = [[float('inf')] * (N+1)] + [[float('inf')] + list(map(int,input().split())) for _ in range(N)]
    cost_mat = [[float('inf')]*(N+1) for _ in range(N+1)]
    # [print(*row) for row in matrix]
    tunnels = {}
    pq = PriorityQueue()
    for _ in range(M):
        ai, aj, bi, bj, c = map(int, input().split())
        tunnels[(bi, bj)] = {'end': (ai, aj), 'cost': c}
        tunnels[(ai, aj)] = {'end': (bi, bj), 'cost': c}
    pq.put([0, (1, 1)])
    cost_mat[1][1] = 0
    while pq.qsize():
        curr = pq.get()
        ci, cj = curr[1]
        if (ci, cj) == (N, N):
            ans = curr[0]
            break
        next_nodes = getEdge(ci, cj)
        print(ci-1, cj-1)
        # print(next_nodes)
        for n in next_nodes:
            ni, nj = n
            next_cost = cal_cost(ci, cj, ni, nj)
            # print(next_cost)
            if cost_mat[ci][cj] + next_cost < cost_mat[ni][nj]:
                pq.put([cost_mat[ci][cj] + next_cost, n])
                cost_mat[ni][nj] = cost_mat[ci][cj] + next_cost
                # heapq.heappush(pq,[cost_mat[ci][cj] + next_cost, n])
    # [print(*row) for row in cost_mat]
    # print(cost_mat)

    # print(tunnels)
    # print(matrix)
#     print(tunnels)
    print(f'#{t} {ans}')
