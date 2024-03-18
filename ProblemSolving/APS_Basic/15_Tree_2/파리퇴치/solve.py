import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    min_kill = float('inf')
    for i in range(N-M+1):
        for j in range(N-M+1):
            local_sum = 0
            for p in range(i, i+M):
                for q in range(j, j+M):
                    # print(i, j, p, q)
                    local_sum  = local_sum + matrix[p][q]
            if local_sum%2 == 0 and local_sum < min_kill:
                # print(p, q)
                min_kill = local_sum
    print(f'#{t} {min_kill}')