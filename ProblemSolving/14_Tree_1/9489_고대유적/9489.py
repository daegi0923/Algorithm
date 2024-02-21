import sys

sys.stdin = open('input.txt')

di = [0, 1]
dj = [1, 0]
def search_max(i, j, curr_len, direction):
    global max_len
    visited[i][j] = 1
    next_i = i + di[d]
    next_j = j + dj[d]
    if 0<=next_i<N and 0<=next_j<M and matrix[next_i][next_j] == 1:
        search_max(next_i, next_j, curr_len+1, direction)
    else:
        if max_len < curr_len:
            max_len = curr_len
        return max_len
    visited[i][j] = 0

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    max_len = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                for d in range(2):
                    search_max(i, j, 1, d)
    print(f'#{t} {max_len}')
