import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(T):
    N = int(input())
    num_lst = list(map(int, input().split()))
    min_num = num_lst[0]
    max_num = num_lst[0]
    for num in num_lst:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    print(f'#{t+1} {max_num-min_num}')
