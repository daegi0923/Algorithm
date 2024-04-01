def dfs(cnt, curr):
    global ans
    if cnt == N:
        ans = ans + 1
        return
    for idx, weight in enumerate(lst):
        if not used[idx] and curr + weight - K >= 500:
            used[idx] = 1
            dfs(cnt + 1, curr + weight - K)
            used[idx] = 0



N, K = map(int, input().split())
lst = list(map(int, input().split()))
used = [0] * (N+1)
ans = 0
dfs(0, 500)
print(ans)