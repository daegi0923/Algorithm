import sys

sys.stdin = open('input.txt')

def isIn(x, y):
    global N
    if 0<=x<N and 0<=y<N:
        return True
    else:
        return False

def othello(i, j, color):
    if color == 1:
        op_side = 2
    else:
        op_side = 1
    matrix[i][j] = color
    for d in range(8):
        change = []
        next_i = i
        next_j = j
        flag = 0
        while True:
            next_i = next_i + di[d]
            next_j = next_j + dj[d]
            if not isIn(next_i, next_j):
                break
            if matrix[next_i][next_j] == color:
                flag = 1
                break
            if not matrix[next_i][next_j]:
                break
            change.append((next_i, next_j))
        if flag:
            for c in change:
                ci, cj = c
                matrix[ci][cj] = color


di = [1, -1, 0, 0, 1, 1, -1, -1]
dj = [0, 0, 1, -1, -1, 1, 1, -1]
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [[0]*N for _ in range(N)]
    matrix[N//2][N//2] = matrix[N//2-1][N//2-1] = 2
    matrix[N//2-1][N//2] = matrix[N//2][N//2-1] = 1
    for _ in range(M): # 1 : 흑돌, 2 : 백돌
        j, i , stone = list(map(int, input().split()))
        othello(i-1, j-1, stone)
    black = white = 0
    for row in matrix:
        black = black + row.count(1)
        white = white + row.count(2)
    print(f'#{t} {black} {white}')