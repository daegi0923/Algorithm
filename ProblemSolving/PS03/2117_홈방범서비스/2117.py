import sys

sys.stdin = open('input.txt')

def count_protect(i, j, k):
    cnt = 0
    for p in range(-k+1, k):
        for q in range(-k+abs(p)+1, k-abs(p)):
            if 0<= i+p < N and 0 <= j+q < N and matrix[i+p][j+q]:
                cnt = cnt + 1
    return cnt


T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N+2):
                local_cnt = count_protect(i, j, k)
                if local_cnt >= ans and local_cnt*M >= k*k + (k-1)*(k-1):
                    ans = local_cnt
    print(f'#{t} {ans}')