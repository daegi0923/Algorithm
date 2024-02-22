import sys

sys.stdin = open('input.txt')

di = [1, 0, 0, -1]
dj = [0, 1, -1, 0]
def dfs(ci ,cj, sum_cost, depth):
    global min_cost, cnt
    cnt = cnt + 1
    depth = depth + 1
    print(ci, cj, sum_cost, min_cost)
    [print(*row) for row in visited]
    if (ci, cj) in[(N - 2, N - 1), (N - 1, N - 2)]:
        if min_cost > sum_cost:
            min_cost = sum_cost
        return
    if min_cost <= sum_cost:
        return
    curr_h = matrix[ci][cj]
    if (ci, cj) in tunnels:
        next_i, next_j = tunnels[(ci, cj)]['end']
        cost = tunnels[(ci, cj)]['cost']
        if cost + sum_cost < min_cost and not visited[next_i][next_j]:
            visited[next_i][next_j] = depth
            dfs(next_i, next_j, sum_cost+cost, depth)
            visited[next_i][next_j] = 0
    nexts = []
    for d in range(4):
        next_i = ci + di[d]
        next_j = cj + dj[d]
        if 0<=next_i<N and 0<=next_j<N:
            nexts.append((next_i, next_j))
    nexts.sort(key = lambda x : abs(matrix[x[0]][x[1]]-matrix[ci][cj]))

    # print(nexts)
    # print(list(map(lambda x : abs(matrix[x[0]][x[1]]-matrix[ci][cj]), nexts)))
    for next_i, next_j in nexts:
        if 0<=next_i<N and 0<=next_j<N and not visited[next_i][next_j]:
            next_h = matrix[next_i][next_j]
            if curr_h < next_h:
                cost = 2 * (next_h-curr_h)
            elif curr_h > next_h:
                cost = 0
            else:
                cost = 1
            if cost + sum_cost < min_cost:
                visited[next_i][next_j] = depth
                dfs(next_i, next_j, sum_cost+cost, depth)
                visited[next_i][next_j] = 0


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    cost_mat = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    tunnels  = {}
    min_cost = float('inf')
    for _ in range(M):
        ai, aj, bi, bj, c = map(int,input().split())
        tunnels[(ai-1, aj-1)] = {'end' : (bi-1, bj-1), 'cost' : c}
        tunnels[(bi-1, bj-1)] = {'end' : (ai-1, aj-1), 'cost' : c}
    # print(matrix)
    # print(tunnels)
    cnt = 0
    dfs(0, 0, 0, 1)
    print(cnt)
    print(f'#{t} {min_cost}')

