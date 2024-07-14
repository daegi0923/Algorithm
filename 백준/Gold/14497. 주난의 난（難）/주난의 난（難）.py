import sys
from collections import deque

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
# print(matrix)
visited = [[0]*M for _ in range(N)]
x1 = x1 - 1
y1 = y1 - 1
x2 = x2 - 1
y2 = y2 - 1
q = deque()
di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]
q.append([x1, y1])
visited[x1][y1] = 1
ans = 0
flag = 0
while q:
    ci, cj = q.popleft()
    # print(ci, cj)
    for d in range(4):
        ni = ci + di[d]
        nj = cj + dj[d]
        if 0 <= ni < N and 0 <= nj < M:
            if not visited[ni][nj]:
                if matrix[ni][nj] == '0':
                    q.appendleft([ni, nj])
                    visited[ni][nj] = visited[ci][cj]
                else:
                    matrix[ni][nj] = '0'
                    q.append([ni, nj])
                    visited[ni][nj] = visited[ci][cj] + 1
    if flag:
        break
# [print(*row) for row in visited]
print(visited[x2][y2]-1)