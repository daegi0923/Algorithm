


def dfs(idx, curr, local_sum, curr_dir):
    global ans
    # print(idx, curr, curr_dir)
    if idx == N:
        if ans > local_sum:
            ans = local_sum
        return
    for ni in range(M):
        if abs(ni-curr)>=2:
            continue
        if curr_dir == ni-curr:
            continue
        dfs(idx+1, ni, local_sum+matrix[idx][curr], ni-curr)

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')
for i in range(M):
    dfs(0, i, 0, 2)

print(ans)