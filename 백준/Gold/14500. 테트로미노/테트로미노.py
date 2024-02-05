def tetro_sum(tetros, matrix, i, j, transpose = False): #True면 2*3 False면 3*2
    sums = []
    for tetro in tetros:
        di, dj = tetro
        tetro_max = [0] * 3 # 그대로, 가로대칭, 세로대칭
        if transpose:
            for d in range(4):
                tetro_max[0] = tetro_max[0] + matrix[i + dj[d]][j + di[d]]

        else:
            for d in range(4):
                tetro_max[0] = tetro_max[0] + matrix[i + di[d]][j + dj[d]]

        sums.append(max(tetro_max))
        # if max(sums) == 210:
        #     print(i, j, transpose, sums)
    return max(sums)


def check(matrix, i, j, N, M):
    local_max = 0
    if j <= M-4:
        local_max = max(local_max, sum(matrix[i][j:j+4]))
        # print(matrix[i][j:j+4],sum(matrix[i][j:j+4]) )
    if i <= N-4:
        axis_y = [matrix[i+d][j] for d in range(4)]
        local_max = max(local_max, sum(axis_y))
        # print(local_max)

    if i <= N-2 and j <= M-2:
        local_max = max(local_max, sum([matrix[i+square_x[d]][j+square_y[d]] for d in range(4)]))
    if i <= N-3 and j <= M-2: # 2x3
        local_max = max(local_max, tetro_sum(tetros, matrix, i, j, transpose=False))
    if i <= N-2 and j <= M-3: # 3*2
        local_max = max(local_max, tetro_sum(tetros, matrix, i, j, transpose=True))
    # print(local_max, i, j)
    return local_max


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
pol1_x = [0, 1, 2, 3] # vector
pol1_y = [0, 1, 2, 3]

square_x = [0, 1, 1, 0] # square
square_y = [0, 0, 1, 1]
tetros = []
tetro1_i = [0, 1, 1, 2] # 번개
tetro1_j = [1, 0, 1, 0]
tetros.append((tetro1_i, tetro1_j))
tetro2_i = [0, 0, 1, 2] # 니은
tetro2_j = [0, 1, 0, 0]
tetros.append((tetro2_i, tetro2_j))

tetro3_i = [0, 1, 1, 2] # 빠큐
tetro3_j = [0, 0, 1, 0]
tetros.append((tetro3_i, tetro3_j))

tetro4_i = [0, 1, 1, 2] # 번개2
tetro4_j = [0, 0, 1, 1]
tetros.append((tetro4_i, tetro4_j))

tetro5_i = [0, 1, 2, 2] # 니은2
tetro5_j = [0, 0, 0, 1]
tetros.append((tetro5_i, tetro5_j))

tetro6_i = [0, 1, 1, 2] # 빠큐2
tetro6_j = [1, 1, 0, 1]
tetros.append((tetro6_i, tetro6_j))

tetro7_i = [0, 0, 1, 2] # 니은3
tetro7_j = [0, 1, 1, 1]
tetros.append((tetro7_i, tetro7_j))

tetro8_i = [0, 1, 2, 2] # 니은4
tetro8_j = [1, 1, 0, 1]
tetros.append((tetro8_i, tetro8_j))




ans = 0
for i in range(N):
    for j in range(M):
       ans = max(ans, check(mat, i, j, N, M))
print(ans)