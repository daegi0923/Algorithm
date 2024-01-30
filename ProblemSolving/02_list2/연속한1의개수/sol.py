import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    seq = list(map(int, input()))
    max_len = 0
    curr_len = 0
    for idx, num in enumerate(seq[1:]):
        if num == 1:
            curr_len = curr_len + 1
        else:
            curr_len = 0

        if max_len < curr_len:
            max_len = curr_len
    print(f'#{t+1} {max_len}')


