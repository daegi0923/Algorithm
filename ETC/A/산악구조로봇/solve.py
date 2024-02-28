import sys
sys.stdin = open('input.txt')


import heapq

def cal_cost(start_i, start_j, end_i, end_j):
    if (start_i, start_j) in tunnels:
        # print(tunnels[(start_i, start_j)])
        tunnel_lst = tunnels[(start_i, start_j)]
        for tunnel in tunnel_lst:
            if tunnel['end'] == (end_i, end_j):
                return tunnel['cost']
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
        for t_num, tunnel in enumerate(tunnels[(i, j)]):
            # print(t_num, tunnel)
            # print(tunnels[(i, j)][0])
            next_nodes.append(tunnels[(i, j)][t_num]['end'])
    return next_nodes
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
#     if t == 13:
#         print(N, M)
    matrix = [list(map(int,input().split())) for _ in range(N)]
    cost_mat = [[float('inf')]*N for _ in range(N)]
    tunnels = {}
    # print(tunnels)
    min_cost = float('inf')
    pq = []
#     if t == 13:
#         [print(*row) for row in matrix]
    for _ in range(M):
        ai, aj, bi, bj, c = map(int,input().split())
        if (ai-1, aj-1) not in tunnels:
            tunnels[(ai-1, aj-1)] = []
        tunnels[(ai-1, aj-1)].append({'end': (bi-1, bj-1), 'cost':c})
        if (bi-1, bj-1) not in tunnels:
            tunnels[(bi-1, bj-1)] = []
        tunnels[(bi-1, bj-1)].append({'end': (ai-1, aj-1), 'cost':c})
    # print(tunnels)

    cost_mat[0][0] = 0
    pq.append([0, (0, 0)])
    cnt = 0
    # print(tunnels)
    while pq:

        curr = heapq.heappop(pq)
        # print(curr)
        ci, cj = curr[1]
        # if cost_mat[ci][cj] > curr[0]:
        #     cost_mat[ci][cj] = curr[0]
        # else:
        #     continue
        if (ci, cj) == (N-1, N-1):
            break
        # print(ci, cj)
        cnt = cnt + 1
        nexts = getEdge(ci, cj)
        # print(nexts)
        for n in nexts:
            ni, nj = n
            next_cost = cal_cost(ci, cj, ni, nj)

            # print(next_cost)
            if cost_mat[ci][cj] + next_cost < cost_mat[ni][nj]:
                cost_mat[ni][nj] = cost_mat[ci][cj] + next_cost
                heapq.heappush(pq,[cost_mat[ci][cj] + next_cost, n])
    # [print(*row) for row in cost_mat]
    print(f'#{t} {cost_mat[N-1][N-1]}')