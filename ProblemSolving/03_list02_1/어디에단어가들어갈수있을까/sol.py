import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N): # 행 우선 순회
        seq = 0
        for j in range(N):
            if mat[i][j] == 1:
                seq = seq + 1
                if j == N-1 and seq == K:
                    ans = ans + 1
            else:
                if seq == K:
                    ans = ans + 1
                seq = 0
    for j in range(N): # 열 우선 순회
        seq = 0
        for i in range(N):
            if mat[i][j] == 1:
                seq = seq + 1
                if i == N-1 and seq == K:
                    ans = ans + 1
            else:
                if seq == K:
                    ans = ans + 1
                seq = 0

    print(f"#{t+1} {ans}")