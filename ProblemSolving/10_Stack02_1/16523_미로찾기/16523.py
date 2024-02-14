import sys
from collections import deque


sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[0]* N for _ in range(N)]
    ans = 0
    direction = [(1,0), (0,1), (-1,0), (0,-1)] # 하우상좌
    for row_num, row in enumerate(maze):
        if '2' in row:
            start = (row_num, row.find('2'))
        if '3' in row:
            goal = (row_num, row.find('3'))
    stack = deque([start])

    while stack:
        curr_x, curr_y = stack[-1]
        for dx, dy in direction:
            next_x, next_y = curr_x + dx, curr_y + dy
            if 0 <= next_x < N and 0 <= next_y < N and maze[next_x][next_y] != '1' and not visited[next_x][next_y]:
                curr_x, curr_y = next_x, next_y
                visited[curr_x][curr_y] = 1
                stack.append((curr_x, curr_y))
                break
        else:
            stack.pop()
        if maze[curr_x][curr_y] == '3':
            ans = 1
            break

    print(f'#{t+1} {ans}')