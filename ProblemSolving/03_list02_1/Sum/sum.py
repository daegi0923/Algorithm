import sys


sys.stdin = open("input.txt")

for _ in range(10):
    t = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]
    row_sum = [0] * 100
    col_sum = [0] * 100
    diag_sum = neg_diag_sum = 0
    for i in range(100):
        for j in range(100):
            row_sum[i] = row_sum[i] + mat[i][j]
            col_sum[j] = col_sum[j] + mat[i][j]
            if i + j == 100:
                neg_diag_sum = neg_diag_sum + mat[i][j]
            if i == j:
                diag_sum = diag_sum + mat[i][j]
    ans = max(*row_sum, *col_sum, diag_sum, neg_diag_sum)
    print(f'#{t} {ans}')