di_even = [-1, -1, -1, 0, 1, 0]
dj_even = [-1, 0, 1, 1, 0,-1]
di_odd = [0,-1, 0, 1, 1, 1]
dj_odd = [-1, 0, 1, 1, 0, -1]


def dfs(i, j, room, price):
    global max_price
    visited[i][j] = 1
    if room == 3:
        if max_price < price:
            max_price = price
        return
    if j%2 == 0:
        di, dj = di_even, dj_even
    else:
        di, dj = di_odd, dj_odd
    for d in range(6):
        if 0 <= i + di[d] < N and 0<=j + dj[d] <M:
            next_i = i + di[d]
            next_j = j + dj[d]
            if not visited[next_i][next_j]:
                dfs(next_i, next_j, room+1, price + honey[next_i][next_j])
                visited[next_i][next_j] = 0
    visited[i][j] = 0


def extraSearch(i, j):
    global max_price
    if j % 2 == 0:
        di, dj = di_even, dj_even
    else:
        di, dj = di_odd, dj_odd
    sum1 =  sum2 = honey[i][j]
    for d in range(6):
        if d%2 == 0 and 0 <= i + di[d] < N and 0<=j + dj[d] <M:
            sum1 = sum1 + honey[i + di[d]][j + dj[d]]
        if d%2 == 1 and 0 <= i + di[d] < N and 0 <= j + dj[d] < M:
            sum2 = sum2 + honey[i + di[d]][j + dj[d]]

    if sum1 > max_price:
        max_price = sum1
    if sum2 > max_price:
        max_price = sum2

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    honey = [list(map(int , input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    max_price = 0
    for i in range(N):
        for j in range(M):

            dfs(i, j, 0, honey[i][j])
            extraSearch(i, j)
    print(f'#{t} {max_price}')
