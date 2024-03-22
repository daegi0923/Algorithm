import sys

sys.stdin = open('input.txt')

import heapq

def cal_dist(i1, i2):
    return ((lst_x[i1]-lst_x[i2])**2 + (lst_y[i1]-lst_y[i2])**2)*E

T = int(input())
for t in range(1, T+1):
    N = int(input())
    # print(N)
    lst_x = list(map(int, input().split()))
    lst_y = list(map(int, input().split()))
    E = float(input())
    hq = [[0, 0]]
    ans = 0
    visited = [0] * (N+1)
    while hq:
        if sum(visited) == N:
            break
        weight, curr = heapq.heappop(hq)
        if not visited[curr]:
            ans = ans + weight
            visited[curr] = 1
            for nxt in range(N):
                if not visited[nxt]:
                    heapq.heappush(hq, [cal_dist(curr, nxt), nxt])
    print(f'#{t} {round(ans)}')