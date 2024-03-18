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
    N, M = map(int,input().split())
    mat = [list(input()) for _ in range(N)]
    pws = []
    for row_num, row in enumerate(mat):
        row = list(map(lambda x : int(x, 16), row))
        row = list(map(lambda x:bin(x)[2:], row))
        row = list(map(lambda x: (4-len(x)) * '0' + x, row))
        line = ''.join(row)
        # print(line)
        if '1' not in line:
            continue
        check = 4*M
        for i in range(4*(M-1), -1, -1):
            curr = line[i]
            if curr == '1' and i < check:
                min_len = M
                pw = line[i-55:i+1]
                # print(pw)
                lens = set(pw.split('0'))
                for ls in lens:
                    if 0 < len(ls) < min_len:
                        min_len = len(ls)
                check = i+1-56*min_len+1
                if check > 0:
                    pw = line[i+1-56*min_len:i+1]
                    pw_lst = [n for idx, n in enumerate(pw) if idx%min_len ==0]
                    if ''.join(pw_lst) not in pws:
                        # print(min_len)
                        # print(i+1-56*min_len, i+1, min_len, len(pw_lst), row_num)
                        # print(''.join(pw_lst))
                        pws.append(''.join(pw_lst))
    ans = 0
    for password in pws:
        if not password:
            continue
        password = [num_code.get(password[i * 7:(i + 1) * 7], 1) for i in range(8)]
#         print(password)
        # password = list(map(num_code.get, password))
        check = 0
        for idx, num in enumerate(password):
            if idx % 2:
                check = check + num
            else:
                check = check + 3 * num
        if check % 10:
            ans = ans
        else:
            ans = ans + sum(password)
    print(f'#{t} {ans}')