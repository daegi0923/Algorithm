import sys

sys.stdin = open('input.txt')
num_code = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    pw = 0
    for row_num, row in enumerate(matrix):
        if '1' not in row:
            continue
        for col_num in range(M-1, -1, -1):
            if row[col_num] == '1':
                pw = row[col_num-55: col_num+1]
                break
        if pw:
            break
    password = [num_code.get(pw[i*7:(i+1)*7]) for i in range(8)]
    # password = list(map(num_code.get, pw_lst))
    check = 0
    for idx, num in enumerate(password):
        if idx%2:
            check = check + num
        else:
            check = check + 3*num
    if check%10:
        ans = 0
    else:
        ans = sum(password)
    print(f'#{t} {ans}')