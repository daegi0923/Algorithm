from collections import deque

def bfs(si, sj):
    global cnt
    q = deque()
    q.append([si, sj])
    while q:
        ci, cj = q.popleft()
        for d in range(8):
            if 0 <= ci + di[d] < M and 0 <= cj + dj[d] < N and matrix[ci + di[d]][cj+dj[d]]:
                q.append([ci + di[d], cj+dj[d]])
                matrix[ci + di[d]][cj+dj[d]] = 0

    cnt = cnt + 1


M, N = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(M)]
# print(matrix)
# print(visited)
di = [0, 0, 1, -1, 1, 1, -1, -1]
dj = [1, -1, 0, 0, 1, -1, -1, 1]
cnt = 0
for i in range(M):
    for j in range(N):
        if matrix[i][j]:
            bfs(i, j)
print(cnt)