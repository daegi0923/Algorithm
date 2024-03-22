import sys

sys.stdin = open('input.txt')

def dfs(curr, cnt):
    global ans
    if curr >= N-1:
        if cnt < ans:
            # print(curr, cnt)
            ans = cnt
        return
    for n_pos in range(lst[curr], 0, -1):
        if cnt < ans:
            dfs(curr+n_pos, cnt + 1)

T = int(input())
for t in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = float('inf')
    lst = lst[1:]
    dfs(0, 0)
    # print(N, lst)
    print(f'#{t} {ans-1}')