import sys

sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N = int(input())
    mat = [list(input().split()) for _ in range(N)]
    mat_90 = [[mat[N-1-j][i] for j in range(N)]for i in range(N)]
    mat_180 = [[mat_90[N-1-j][i] for j in range(N)]for i in range(N)]
    mat_270 = [[mat_180[N-1-j][i] for j in range(N)]for i in range(N)]
    mats = [mat_90, mat_180, mat_270]
    ans = [[''.join(mats[i][j]) for i in range(3)]for j in range(N)]
    print(f'#{t+1}')
    # [print(*row) for row in ans]

    ans = []
    for j in range(N):
        row = []
        for i in range(3):
            row.append(''.join(mats[i][j]))
        ans.append(row)
    print(ans)
