def cal_dist(len_chickens):
    dist = [float('inf')] * len(houses)
    for chicken_num in range(len_chickens):
        if used[chicken_num]:
            c_i, c_j = chickens[chicken_num]
            for idx in range(len(houses)):
                h_i, h_j = houses[idx]
                if abs(h_i - c_i) + abs(h_j - c_j) <dist[idx]:
                    dist[idx] = abs(h_i - c_i) + abs(h_j - c_j)
    # print(dist, used)
    return sum(dist)

def dfs(curr, cnt, n_chickens):
    global ans
    if cnt == M or curr == n_chickens:
        local_ans = cal_dist(n_chickens)
        if local_ans < ans:
            # print(used)
            ans = local_ans
        return
    # print(curr, len(chickens))
    used[curr] = 1
    dfs(curr+1, cnt+1, n_chickens)
    used[curr] = 0
    dfs(curr+1, cnt, n_chickens)

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            chickens.append((i, j))
        elif matrix[i][j] == 1:
            houses.append((i, j))
used = [0] * len(chickens)
ans = float('inf')
dfs(0, 0, len(chickens))
print(ans)

