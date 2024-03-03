import sys
from collections import deque

sys.stdin = open('input.txt')

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
dmat = [[3, 0, 1, 2],
        [0, 1, 2, 3],
        [1, 2, 3, 0],
        [2, 3, 0, 1]
]
def getHarvest(si, sj, direction):
    local_sum = 0
    harvestMat = [[1]*N for _ in range(N)]
    grow = {}
    for day in range(M):
        if not matrix[si][sj]:
            for d in dmat[direction]:
                ni = si + di[d]
                nj = sj + dj[d]
                if not matrix[ni][nj] or matrix[ni][nj] >= 2*(3+harvestMat[ni][nj]):
                    grow[(si, sj)] = 1
                    break
        if matrix[si][sj] >= 2*(3+harvestMat[si][sj]):
            matrix[si][sj] = 0
            harvestMat[si][sj] = harvestMat[si][sj] + 1
            grow[(si, sj)] = 0
            local_sum = local_sum + 1
        for d in dmat[direction]:
            ni = si + di[d]
            nj = sj + dj[d]
            if not matrix[ni][nj] or matrix[ni][nj] >= 2 * (3 + harvestMat[ni][nj]):
                si, sj = ni, nj
                direction = d
                break
        for point in grow:
            if grow[point]:
                p, q = point
                matrix[p][q] = matrix[p][q] + 2

    for point in grow:
        p, q = point
        matrix[p][q] = 0
    return local_sum


T =  int(input())
for t in range(1 ,T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if not matrix[i][j]:
                for sd in range(4):
                    res = getHarvest(i, j, sd)
                    if res > ans:
                        ans = res

    print(f'#{t} {ans}')