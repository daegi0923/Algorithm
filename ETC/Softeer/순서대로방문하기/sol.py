import sys

sys.stdin = open('input.txt')



di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(ci ,cj, gi, gj, k):
    global ans
    if [ci, cj] in points:
        stack.append([ci, cj])
    if ci == gi and cj == gj:
        print(stack, points)
        if stack == points:
            ans = ans + 1
        return
    for d in range(4):
        nxt_i = ci + di[d]
        nxt_j = cj + dj[d]
        if 0 <= nxt_i < n and 0 <= nxt_j < n and not visited[nxt_i][nxt_j] and not mat[nxt_i][nxt_j]:
            visited[nxt_i][nxt_j] = 1
            dfs(nxt_i, nxt_j, gi, gj, k+1)
            if stack[-1] == [nxt_i, nxt_j]:
                stack.pop()
            visited[nxt_i][nxt_j] = 0


n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
points = []
paths = [0]*m
paths[0] = 1
ans = 0
visited = [[0] * n for _ in range(n)]
stack = []
for _ in range(m):
    i, j = map(int, input().split())
    points.append([i-1, j-1])
si, sj = points[0]
gi, gj = points[-1]
visited[si][sj] = 1
dfs(si, sj, gi, gj, 1)
print(ans)