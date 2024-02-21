import sys


sys.stdin = open('input.txt')
def is_available(start, map):
    lst = []
    dirs = [(1, 0),(-1, 0),(0, 1),(0, -1)]
    # [print(*row) for row in map]
    for dir in dirs:
        i, j = start
        while True:
            if not (0 <= i+dir[0] <= N-1 and 0 <= j+dir[1] <= N-1):
                break
            i, j = i+dir[0], j+dir[1]
            if map[i][j] == 1:
                while 0 <= i+dir[0] < N and 0 <= j+dir[1] < N:
                    i, j = i + dir[0], j+dir[1]
                    lst.append((i, j))
                    if map[i][j] == 1:
                        break
                break


    return lst




def dfs(curr, depth, map_):
    global ans,kill, cnt
    if depth >= 4:
        return
    cnt = cnt + 1
    kill[depth] = False
    y, x = curr
    if map_[y][x] == 1:
        visited.append(curr)
        map_[y][x] = 0
        kill[depth] = (y, x)

    can_go = is_available(curr, map_)

    # print(depth,curr, can_go,  kill)
    # [print(*row) for row in map_]
    if depth <3:
        for pos in can_go:
            y, x = pos
            if depth == 2:
                if map_[y][x] == 1:
                    dfs(pos, depth+1, map_)
            else:
                dfs(pos, depth + 1, map_)

            if kill[depth+1]:
                y, x = kill[depth+1]
                map_[y][x] = 1
#                 print(y, x)
#                 [print(*row) for row in map_]



T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        if 2 in mat[i]:
            start = (i, mat[i].index(2))
    ans = 0
    cnt = 0
    visited = []
    kill = [False]*4
    dfs(start,0, mat)
    print(f'#{t} {len(set(visited))}', cnt)
#     print(set(visited))
    for point in visited:
        i, j = point
        mat[i][j] = '*'
#     [print(*row) for row in mat]