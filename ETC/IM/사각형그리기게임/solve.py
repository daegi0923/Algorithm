import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_area = 0
    ans = 0
    for i in range(N):
        for j in range(N):
            num = matrix[i][j]
            if (N-i) * (N-j) >= max_area:
                for right in range(i, N):
                    for down in range(j, N):
                        if matrix[right][down] == num:
                            area = (right-i+1)*(down-j+1)
                            if max_area == area:
                                ans = ans + 1
                            if max_area < area:
                                max_area = max(area, max_area)
                                ans = 1

    print(f'#{t} {ans}')