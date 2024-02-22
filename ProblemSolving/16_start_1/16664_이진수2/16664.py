import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = float(input())
    ans = ''
    digit_count = 0.5
    while True:
        if len(ans)>13:
            ans = 'overflow'
            break
        if not N:
            break
        if N >= digit_count:
            N = N - digit_count
            ans = ans + '1'
        else:
            ans = ans + '0'
        digit_count = digit_count/2
    print(f'#{t}', ans)