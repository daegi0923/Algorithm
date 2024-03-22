import sys

sys.stdin = open('input.txt')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(p, q, k, num):
    if k == 6:
        res.add(num)
        return
    for d in range(4):
        ni = p+di[d]
        nj = q+dj[d]
        if 0 <= ni < 4 and 0 <= nj < 4:
            visited[ni][nj] = 1
            dfs(ni, nj, k+1, num + str(mat[ni][nj]))
            visited[ni][nj] = 1


T = int(input())
for t in range(1, T+1):
    mat = [list(map(int, input().split())) for _ in range(4)]
    visited = [[0]*4 for _ in range(4)]
    res = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, str(mat[i][j]))
    print(res)
    print(f'#{t} {len(res)}')