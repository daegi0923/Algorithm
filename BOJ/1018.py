def check(board):
    a =  b = 0
    patternB = "BWBWBWBW"
    patternW = "WBWBWBWB"
    for i in range(8):
        for j in range(8):
            if i%2 == 0 and board[i][j] != patternB[j]:
                a += 1
            elif i%2 == 0 and board[i][j] != patternW[j]:
                b += 1
            elif i%2 != 0 and board[i][j] != patternB[j]:
                b += 1
            elif i%2 != 0 and board[i][j] != patternW[j]:
                a += 1
    return min(a, b)

def make_check(board, a, b):
    check_board = []
    for i in range(8):
        line = board[a+i]
        check_board.append(line[b:b+8])
    return check_board

m, n = map(int, input().split())
board = []
ans = 32
for i in range(m):
    board.append(list(input()))
for i in range(m-7):
    for j in range(n-7):
        check_board = make_check(board, i, j)
        count = check(check_board)
        if ans > count:
            ans = count
print(ans)