import sys

sys.stdin = open('input.txt')

def dfs(k, s):
    global ans
    if k == N:
        if s >= B and s-B < ans:
            ans = s-B
        return
    if s < B:
        used[k] = 1
        dfs(k+1, s+lst[k])
        used[k] = 0
    dfs(k+1, s)



T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    used = [0] * (N+1)
    ans = float('inf')
    dfs(0, 0)
    print(f'#{t} {ans}')