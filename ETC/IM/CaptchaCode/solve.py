import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, K = map(int,input().strip().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    idx = 0
    ans = 0
    for num in sample:
        if passcode[idx] == num:
            idx = idx + 1
            if idx == K:
                ans = 1
                break
    print(f'#{t} {ans}')
