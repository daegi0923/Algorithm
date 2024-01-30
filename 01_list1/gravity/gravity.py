import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    gravitys = []
    for idx, height in enumerate(lst):
        cnt = 0
        for dist in range(1, N-idx):
            if height <= lst[idx + dist]:
                cnt = cnt + 1
        gravitys.append(N-1-cnt-idx)
    print(f'#{t+1} {max(gravitys)}')