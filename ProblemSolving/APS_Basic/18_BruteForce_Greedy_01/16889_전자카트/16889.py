import sys
sys.stdin = open('input.txt')

def dfs(n, local_sum, curr):
    global ans
    if n == N-1:
        if local_sum + matrix[curr][0] < ans:
            # print(seq, ans)
            ans = local_sum + matrix[curr][0]
            return
    for i in range(1, N):
        if not visited[i] and matrix[curr][i] + local_sum < ans:
            visited[i] = 1
#             seq.append(i)
            dfs(n+1, matrix[curr][i]+local_sum, i)
            visited[i] = 0
#             seq.pop()

T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    # seq = []
    ans = float('inf')
    dfs(0, 0, 0)
    print(f'#{t} {ans}')