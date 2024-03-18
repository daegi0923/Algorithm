import sys
sys.stdin = open('input.txt')

from collections import deque
T = int(input())
for t in range(1, T+1):
    N, M, K = map(int,input().split())
    arrivals = list(map(int,input().split()))
    arrivals.sort()
    queue = deque()
    idx = 0
    for time in range(0, max(arrivals)+1):
        if len(queue) >= N:
            ans = 'Possible'
            break
        if time > 0  and time%M == 0:
            [queue.append(1) for _ in range(K)]
        if time == arrivals[idx]:
            if queue:
                queue.popleft()
                idx = idx + 1
            else:
                ans = 'Impossible'
                break
    else:
        ans = 'Possible'

    print(f'#{t} {ans}')
