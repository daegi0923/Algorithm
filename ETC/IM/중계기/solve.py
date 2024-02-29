import sys
sys.stdin = open('input.txt')
import math
T = int(input())
for t in range(1, T+1):
    N = int(input())+1
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # i_min, j_min = float('inf')
    # i_max, j_max = 0

    ci, cj = [(row_num, row.index(2)) for row_num, row in enumerate(matrix) if 2 in row][0]
    # print(ci, cj)
    max_r = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                dist = ((ci-i)**2 + (cj-j)**2)**0.5
                if dist > max_r:
                    max_r = dist

    print(f'#{t} {math.ceil(max_r)}')