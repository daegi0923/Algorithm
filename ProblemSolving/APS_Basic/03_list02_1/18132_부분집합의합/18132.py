import sys


sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    ans = 0
    for i in range(1<<12):
        cnt = 0
        sum_set = 0
        for j in range(12):
            if i&(1<<j):
                sum_set = sum_set + j +1
                cnt = cnt + 1


        if cnt == N and sum_set == K:
            ans = ans + 1
    print(f'#{t+1} {ans}')