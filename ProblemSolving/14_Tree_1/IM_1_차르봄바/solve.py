import sys

sys.stdin = open('input.txt')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_virus = 0
    for i in range(N):
        for j in range(N):
            virus = matrix[i][j]
            for d in range(4):
                for p in range(1, P+1):
                    if 0 <= i + p * di[d] < N and 0 <= j + p * dj[d] < N:
                        next_i = i + p * di[d]
                        next_j = j + p * dj[d]
                        virus = virus + matrix[next_i][next_j]
            if virus > max_virus:
                max_virus = virus
    print(f'#{t} {max_virus}')

