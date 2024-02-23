import sys

sys.stdin = open('input.txt')

T = 11
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    matrix = list(map(list, zip(*matrix[::-1]))) # 행렬 회전 1: 왼쪽, 2: 오른쪽
    ans = 0
    shift = 0
    for row in matrix:
        # line = ''.join(map(str,row))
        # line = line.replace('0', '')
        # cnt = line.count('21')
        # ans = ans + cnt

        while True:
            cnt = 0
            for idx, item in enumerate(row):
                if shift:
                    shift = 0
                    continue
                if item == 1:
                    if row[idx - 1] == 0 and 0 < idx < N:
                        row[idx], row[idx-1] = 0, 1
                        cnt  = cnt + 1
                    elif idx == 0:
                        row[0] = 0
                        cnt  = cnt + 1
                elif item == 2:
                    if 0 <= idx < N-1 and row[idx + 1] == 0:
                        row[idx], row[idx+1] = 0, 2
                        cnt  = cnt + 1
                        shift = 1
                    elif idx == N-1:
                        row[N-1] = 0
                        cnt  = cnt + 1
            if cnt == 0:
                # print(row)
                local_sum = ''.join(map(str,row)).count('21')
                # print(''.join(map(str,row)))
                ans = ans + local_sum
                break
    print(f'#{t} {ans}')
    # [print(*row) for row in matrix]

