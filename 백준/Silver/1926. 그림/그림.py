

from collections import deque


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(start_i, start_j):
    global max_cnt
    q = deque([(start_i, start_j)])
    cnt = 0
    while q:
        # print(q)
        curr_i = q[0][0]
        curr_j = q[0][1]
        q.popleft()
        if not visited[curr_i][curr_j]:
            visited[curr_i][curr_j] = 1
            cnt = cnt + 1
        for d in range(4):
            if 0 <= curr_i + dx[d] < N and 0 <= curr_j + dy[d] < M and mat[curr_i + dx[d]][curr_j + dy[d]] == 1 and not visited[curr_i + dx[d]][curr_j + dy[d]]:
                if (curr_i, curr_j) not in q:
                    q.append((curr_i + dx[d], curr_j + dy[d]))

    if cnt > max_cnt:
        max_cnt = cnt
    return


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_cnt = 0
n_of_picture = 0
q = deque()

for row_num, row in enumerate(mat):
    for col_num, item in enumerate(row):
        if item == 1 and not visited[row_num][col_num]:
            n_of_picture = n_of_picture + 1
            bfs(row_num, col_num)
print(n_of_picture)
print(max_cnt)