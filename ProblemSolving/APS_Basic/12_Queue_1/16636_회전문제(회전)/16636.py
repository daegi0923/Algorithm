import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = lst[M%N]
    print(f'#{t} {ans}')