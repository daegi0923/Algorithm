def kill(matrix, a, b, M, N):
    hor = [(x, b) for x in range(a-M+1, a+M) if 0 <= x <= N-1]
    ver = [(a, y) for y in range(b-M+1, b+M) if 0 <= y <= N-1]
    lin = [(a+m, b+m) for m in range(-M+1, M) if 0 <= (a+m) <= N-1 and 0 <= (b+m) <= N-1]
    neg_lin = [(a+m, b-m) for m in range(-M+1, M) if 0 <= (a+m) <= N-1 and 0 <= (b-m) <= N-1]
    cross_cnt = 0
    lin_cnt = 0
    lin_point = 0
    cross_point = 0
    for i in hor+ver:
        x, y = i
        # print(x, y)
        cross_cnt = cross_cnt + matrix[x][y]

    for i in lin + neg_lin:
        x, y = i
        # print(x, y)
        lin_cnt = lin_cnt + matrix[x][y]
    return max(cross_cnt - matrix[a][b], lin_cnt - matrix[a][b])







T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for x in range(N)]
    max_kill = 0
    max_point = 0
    for x, cnt_x in enumerate(matrix):
        for y, cnt_y in enumerate(matrix):
            cnt = kill(matrix, x, y, M, N)
            if cnt > max_kill:
                max_kill = cnt
                max_point = (x, y)
    print(f'#{t} {max_kill}')
    # print(max_point)