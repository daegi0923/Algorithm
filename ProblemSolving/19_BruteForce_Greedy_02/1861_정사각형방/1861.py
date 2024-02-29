import sys
sys.stdin = open('input.txt')


from collections import deque
T = int(input())
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(si, sj, ci, cj, depth):
    global max_room, start_room, end_room
    if depth > max_room:
        max_room = depth
        start_room = matrix[si][sj]
        end_room = matrix[ci][cj]
    elif depth == max_room and start_room > matrix[si][sj]:
        max_room = depth
        start_room = matrix[si][sj]
        end_room = matrix[ci][cj]

    for d in range(4):
        ni = ci + di[d]
        nj = cj + dj[d]
        if 0<=ni<N and 0<=nj<N and matrix[ni][nj] - matrix[ci][cj] == 1:
            dfs(si, sj,ni, nj, depth + 1)



for t in range(1, T+1):
    max_room = 0
    start_room = 0
    end_room = 0
    N = int(input())
    q = deque()
    matrix = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # print(start_room, end_room)
            visited_room = 0
            q.append((i, j))
            while q:
                # print(q, start_room, end_room)
                ci, cj = q.popleft()

                visited_room = visited_room + 1
                for d in range(4):
                    ni = ci + di[d]
                    nj = cj + dj[d]
                    if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] - matrix[ci][cj] == 1 and matrix[ci][cj] not in range(start_room, end_room):
                        q.append((ni, nj))
            if max_room < visited_room:
                max_room = visited_room
                start_room = matrix[i][j]
            if max_room ==  visited_room and start_room > matrix[i][j]:
                max_room = visited_room
                start_room = matrix[i][j]

    print(f'#{t} {start_room} {max_room}')