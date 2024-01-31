import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(N-(M-1)):
        for j in range(N-(M-1)):
            sec_sum = 0
            for k in range(M):
                for l in range(M):
                    sec_sum = sec_sum + mat[i+k][j+l]
            if max_sum < sec_sum:
                max_sum = sec_sum
    print(f"#{t+1} {max_sum}")