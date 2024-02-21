import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = round(N**(1/3), 4)
    if num%int(num) == 0:
        ans = int(num)
    else:
        ans = -1
    print(f'#{t} {ans}')