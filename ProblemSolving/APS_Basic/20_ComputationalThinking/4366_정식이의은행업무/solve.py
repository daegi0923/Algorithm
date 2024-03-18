import sys

sys.stdin = open('input.txt')

def trinary_to_int(string):
    res = 0
    for idx, n in enumerate(string):
        res = res + 3**(len(string)-1-idx)*int(n)
        # print(idx, n, res)
    return res

T = int(input())
for t in range(1, T+1):
    binary = input()
    trinary = input()
    ans = 0
    for b_num, b in enumerate(binary):
        temp_b = list(binary)
        temp_b[b_num] = str(1 - int(temp_b[b_num]))
        for t_num, tri in enumerate(trinary):
            temp_c = list(trinary)
            for num in range(3):
                temp_c[t_num] = num
                # print(temp_b, temp_c)
                # print(''.join(temp_b))
                # print(trinary_to_int(temp_c))
                if int(''.join(temp_b), 2) == trinary_to_int(temp_c):
                    ans = int(''.join(temp_b), 2)
                    break
    print(f'#{t} {ans}')

