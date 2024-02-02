import sys


sys.stdin = open('input.txt')
for _ in range(10):
    t = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]

    ladders = [c for c in range(100) if mat[99][c] >0]
    start = mat[99].index(2)
    ladder_num = ladders.index(start)
    # print(start , ladder_num)
    # print(ladders)
    for r in range(99, -1, -1):
        if start > 0 and mat[r][start-1] == 1:
            ladder_num = ladder_num - 1
            start = ladders[ladder_num]
            continue
        if start < 99 and mat[r][start+1] == 1:
            ladder_num = ladder_num + 1
            start = ladders[ladder_num]
            continue
    ans = 0
    print(f'#{t} {start}')
