from collections import deque
import copy

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(new_map):
    global ans
    q = deque(virus)

    while q:
        ci, cj = q.popleft()
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            if 0 <= ni < N and 0<=nj<M and new_map[ni][nj] == 0:
                if (ni, nj) in walls:
                    continue
                new_map[ni][nj] = 2
                q.append((ni, nj))
    local_ans = sum(row.count(0) for row in new_map) - 3
    if local_ans > ans:
        ans = local_ans
        # [print(*row) for row in new_map]
        # print(ans)
        # print(walls)
    return

def dfs(wall_cnt):
    if wall_cnt == 3:
        bfs(copy.deepcopy(matrix))
        return
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0 and (i, j) not in walls:
                walls.append((i, j))
                dfs(wall_cnt+1)
                walls.pop()

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
walls = []
virus = [(i, j) for i in range(N) for j in range(M) if matrix[i][j] == 2]
ans = 0
dfs(0)
print(ans)