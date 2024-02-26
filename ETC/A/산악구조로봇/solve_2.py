import sys


sys.stdin = open('input.txt')
import heapq

def cal_cost(start_i, start_j, end_i, end_j):
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
        if 0<=next_i < N and 0 <= next_j < N:
            next_nodes.append((next_i, next_j))
    if (i, j) in tunnels:
        next_nodes.append(tunnels[(i, j)]['end'])
    return next_nodes
T = int(input())
for t in range(1, T+1):
    NM = list(map(int, input().split()))
    N = NM[0]
    matrix = [list(map(int,input().split())) for _ in range(N)]
    cost_mat = [[float('inf')]*N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    tunnels  = {}
    min_cost = float('inf')
    pq = []
    M = 0
    if len(NM) == 2:
        M = NM[1]
    for _ in range(M):
        ai, aj, bi, bj, c = map(int,input().split())
        tunnels[(bi-1, bj-1)] = {'end': (ai-1, aj-1), 'cost': c}
        tunnels[(ai-1, aj-1)] = {'end': (bi-1, bj-1), 'cost': c}
    pq.append([0, (0, 0)])
    cnt = 0
    cost_mat[0][0] = 0
    while pq:
        curr = heapq.heappop(pq)
        ci, cj = curr[1]
        cnt = cnt + 1
        nexts = getEdge(ci, cj)
        visited[ci][cj] = 1
        # print(nexts)
        for n in nexts:
            ni, nj = n
            next_cost = cal_cost(ci, cj, ni, nj)
            # print(next_cost)
            if not visited[ni][nj] and cost_mat[ci][cj] +next_cost <  cost_mat[ni][nj]:
                cost_mat[ni][nj] = cost_mat[ci][cj] + next_cost
                heapq.heappush(pq,[cost_mat[ci][cj] + next_cost, n])
    # [print(*row) for row in cost_mat]
    # print(cost_mat)

    # print(tunnels)
    # print(matrix)
    # print(cnt)
    print(f'#{t} {cost_mat[N-1][N-1]}')
