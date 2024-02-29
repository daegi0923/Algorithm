import sys

sys.stdin = open('input.txt')
def dfs(i, local_sum):
    global ans
    if i == N:
        if local_sum == K:
            ans = ans + 1
        return
    if not used[i]:
        if local_sum + lst[i] <= K:
            used[i] = 1
            dfs(i+1, local_sum + lst[i])
            used[i] = 0
        dfs(i+1, local_sum)

    pass
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    used = [0] * (N+1)
    ans = 0
    dfs(0, 0)
    print(f'#{t} {ans}')