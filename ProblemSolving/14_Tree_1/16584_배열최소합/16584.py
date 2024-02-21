import sys
sys.stdin = open('input.txt')
def dfs(i, subset_sum,k):
    global min_sum
    if i == k:
        if subset_sum < min_sum:
            min_sum = subset_sum
        return
    if subset_sum > min_sum:
        return
    for idx in range(N):
        if not visited[idx] and matrix[i][idx] != 1:
            visited[idx] = 1
            dfs(i+1, subset_sum + matrix[i][idx], k)
            visited[idx] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = 10000
    dfs(0, 0, N)
    print(f'#{t} {min_sum}')