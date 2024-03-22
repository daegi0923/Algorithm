import sys

sys.stdin = open('input.txt')

def dfs(k, tot):
    global ans
    if k == N:
        if tot < ans:
            ans = tot
        return
    for fact_num in range(N):
        if not assigned[fact_num] and tot + mat[k][fact_num] <= ans:
            assigned[fact_num] = 1
            dfs(k+1, tot+mat[k][fact_num])
            assigned[fact_num] = 0





T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    assigned = [0] * N

    ans = float('inf')
    dfs(0, 0)
    print(f'#{t} {ans}')