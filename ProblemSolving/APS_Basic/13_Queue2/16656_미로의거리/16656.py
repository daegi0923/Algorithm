import sys

sys.stdin = open('input.txt')

from collections import deque


T = int(input())
dRow = [0, 0, 1, -1]
dCol = [1, -1, 0, 0]
for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for r, row in enumerate(maze):
        if 2 in row:
            start = (r, row.index(2))

        if 3 in row:
            goal = (r, row.index(3))
    # print(start, goal)
    q = deque([[start]])
    dist = 0
    ans = 0
    while q[0]:
        temp = []
        curr = q[0]
        q.popleft()
        if goal in curr:
            ans = dist-1
            break
        dist = dist + 1
        for c in curr:
            i, j = c
            maze[i][j] = 1
            for d in range(4):
                if 0<= i+dRow[d] < N and 0<= j+dCol[d] < N and maze[i+dRow[d]][j+dCol[d]] != 1:
                    temp.append((i+dRow[d], j+dCol[d]))
        q.append(temp)
    print(f'#{t} {ans}')