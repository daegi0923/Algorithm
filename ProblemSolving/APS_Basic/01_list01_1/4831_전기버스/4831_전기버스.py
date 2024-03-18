import sys

sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    K, N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    route = [0] * N
    for num in lst:
        route[num] = 1
    ans = 0
    curr = 0
    while True:
        if curr + K > N-1:
            break
        if 1 not in route[curr+1:curr+K+1]:
            ans = 0
            break
        for k in range(K, 0, -1):
            if curr + k in lst:
                curr = curr + k
                ans = ans + 1
                break
    print(f'#{t+1} {ans}')