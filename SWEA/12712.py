def cross_kill(matrix, a, b, M):
    hor = [(x, b) for x in range(a-M+1, a+M) if x >= 0]
    ver = [(a, y) for y in range(b-M+1, b+M) if y >= 0]
    print(hor, ver)

def x_kill(matrix, a, b, M):
    hor = [(a+m, b+m) for m in range(M+1, M) if x >= 0]
    ver = [(a, y) for y in range(b-M+1, b+M) if y >= 0]



def max_kill_fly(matrix, M):
    max_fly = 0
    for x, cnt_x in enumerate(matrix):
        for y, cnt_y in enumerate(matrix[x]):
            pass






T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for x in range(N)]
    print(cross_kill(matrix, 0, 0, M))        