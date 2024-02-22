# import sys

# sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    direction = [0, 1, 2, 3] #상하우좌
    # 행 : 현재 방향, 열 : 다음 사과의 위치
    # ex) 현재방향 아래쪽, 다음사과 우상이면 dirmat[2][2] 조회해서 다음방향정함
    #0 1 2 3 : 좌상, 좌하, 우상, 우하
    #우회전 횟수 , 다음방향
    dir_matrix = [
        [(3, 3), (3, 3), (1, 2), (2, 1)],
        [(2, 0), (1, 3), (3, 2), (3, 2)],
        [(3, 0), (2, 3), (3, 0), (1, 1)],
        [(1, 0), (3, 1), (2, 2), (3, 1)]
    ]
    ans = 0
    max_apple = max(max(row) for row in mat)

    apples = [0] * (max_apple+1)
    apples[0] = (0, 0)
    for r, row in enumerate(mat):
        for c, num in enumerate(row):
            if num > 0:
                apples[num] = (r, c)
    pos_i = 0
    pos_j = 0
    curr_dir = 2
    for point in apples[1:]:
        next_i, next_j = point
        if pos_j < next_j:# 우
            if pos_i < next_i: #우하
                next_pos = 3
            else:#우상
                next_pos = 2
        else: # 좌
            if pos_i < next_i: #좌하
                next_pos = 1
            else:#좌상
                next_pos = 0
        cnt, curr_dir = dir_matrix[curr_dir][next_pos]
        # print(curr_dir, cnt)
        ans = ans + cnt
        pos_i, pos_j = next_i, next_j
    print(f'#{t+1} {ans}')


