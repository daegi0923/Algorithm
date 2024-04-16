R, C, N = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
time_matrix = [[0]*C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if matrix[r][c] == 'O':
            time_matrix[r][c] = 3
time = 0
while True:
    if time == N:
        break
    if time and time % 2:
        for r in range(R):
            for c in range(C):
                if time_matrix[r][c] == 0:
                    time_matrix[r][c] = 4
    bomb_set = set()
    for r in range(R):
        for c in range(C):
            if time_matrix[r][c] == 1:
                # print(r, c)
                # print(max(0, r-1), min(r+1, R))
                # print(max(0, c - 1), min(c + 1, C))
                for nr in range(max(0, r-1), min(r+2, R)):
                    bomb_set.add((nr,c))
                for nc in range(max(0, c - 1), min(c + 2, C)):
                    bomb_set.add((r,nc))
                # print(time_matrix)
            else:
                time_matrix[r][c] = max(0, time_matrix[r][c] - 1)

    time = time + 1
    for b in bomb_set:
        i, j = b
        time_matrix[i][j] = 0
    # [print(*row) for row in time_matrix]
    # print(time)

ans = [['.']*C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if time_matrix[r][c]:
            ans[r][c] = 'O'
[print(''.join(row)) for row in ans]

