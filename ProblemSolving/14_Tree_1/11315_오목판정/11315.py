import sys

sys.stdin = open('input.txt')

di = [0, 1, 1, 1]
dj = [1, -1, 0, 1]
def dfs(i, j, direction, depth):
    global ans
    if depth == 4:
        ans = 1
        return
    # print(i, j, depth)
    next_i = i + di[direction]
    next_j = j + dj[direction]
    if 0<= next_i < N and 0<=next_j<N and go[next_i][next_j] == 'o':
        dfs(next_i, next_j, direction, depth+1)
    return



T = int(input())
for t in range(1, T+1):
    N = int(input())
    go = [list(input()) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if ans:
                break
            if go[i][j] == 'o':
                for d in range(4):
                    dfs(i, j, d, 0)
    if ans:
        res = 'YES'
    else:
        res = 'NO'
    print(f'#{t} {res}')