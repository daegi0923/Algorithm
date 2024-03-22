import sys

sys.stdin = open('input.txt')

import heapq

T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([w, e])
    cost_map = [float('inf')] * (N+1)
    cost_map[0] = 0
    hq = [[0, 0]]

    while hq:
        curr_weight, curr = heapq.heappop(hq)
        nexts = graph[curr]
        for n in nexts:
            next_weight, next = n
            if curr_weight + next_weight < cost_map[next]:
                cost_map[next] = curr_weight + next_weight
                hq.append([curr_weight+ next_weight, next])
    print(f'#{t} {cost_map[N]}')