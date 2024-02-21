import sys
from collections import deque
sys.stdin = open('input.txt')

dRow = [0, 0, 1, -1]
dCol = [1, -1, 0, 0]
for _ in range(10):
    t = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = []
    sRow = 1
    sCol = 1
    ans = 0
    q = deque([(sRow, sCol)])
    while q:
        i, j = q[0]
        q.popleft()
        # print(i, j)
        if maze[i][j] == 3:
            ans = 1
            break
        visited.append((i,j))
        for d in range(4):
            next_i, next_j = i + dRow[d], j+dCol[d]
            if maze[next_i][next_j] != 1 and (next_i, next_j) not in visited:
                q.append((next_i, next_j))
    print(f'#{t} {ans}')