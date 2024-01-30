import sys


sys.stdin = open('input.txt')


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    max_num = sum(num_lst[0:M])
    min_num = sum(num_lst[0:M])

    for idx, num in enumerate(num_lst[0:N-M+1]):
        near = num_lst[idx:idx+M]
        partial_sum = sum(near)
        if max_num < partial_sum:
            max_num = partial_sum
        if min_num > sum(near):
            min_num = partial_sum
    print(f'#{t+1} {max_num - min_num}')
