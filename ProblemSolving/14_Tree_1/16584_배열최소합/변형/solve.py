import sys

sys.stdin = open('input.txt')

def dfs(n, k, local_sum):
    global ans
    if n == k:
        if local_sum < ans:
            # print(visited, local_sum)
            ans = local_sum
        return
    for i in range(N):
        if not visited[i] or (n+1 in nums):
            if not n+1 in nums:
                visited[i] = 1
            dfs(n+1, k, local_sum + matrix[n][i])
            visited[i] = 0





T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = float('inf')
    dfs(0, N, 0)
    print(f'#{t} {ans}')