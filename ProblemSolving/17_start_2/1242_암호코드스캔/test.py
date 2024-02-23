import sys

sys.stdin = open('input.txt')

dict_ = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
         '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
         '0110111': 8, '0001011': 9}
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    code_hex_list = set()
    sum_ = 0
    thick = (M * 4) // 56
    decode_list = []
    new_dict = {}

    for th in range(1, thick + 1):
        for key, value in dict_.items():
            temp = ''
            for char_ in key:
                temp += char_ * th

            new_dict[temp] = value

    for _ in range(N):
        code_hex_list.add(input().strip())

    for idx, code_hex in enumerate(code_hex_list):
        if not code_hex:
            continue

        code_bin = ''.join([format(int('0x' + num, 16), '04b') for num in code_hex])
        # print(code_bin)

        for th in range(1, thick + 1):
            for i in range(M * 4 - 56 * th):
                if code_bin[i: i + 7 * th] not in new_dict:
                    continue

                temp = code_bin[i: i + 56 * th]

                chk = [temp[7 * th * j: 7 * th * j + 7 * th] for j in range(8)]

                if all(chk[k] in new_dict for k in range(8)):
                    decode = [new_dict[num] for num in chk]

                    if decode not in decode_list:
                        print(decode)
                        print(i,  i + 56 * th, th, idx)
                        decode_list.append(decode)

    for decode in decode_list:
        # print(decode)
        result = sum(3 * num if i % 2 == 0 else num for i, num in enumerate(decode))

        if result % 10 == 0:
            sum_ += sum(decode)

    print(f'#{tc + 1} {sum_}')