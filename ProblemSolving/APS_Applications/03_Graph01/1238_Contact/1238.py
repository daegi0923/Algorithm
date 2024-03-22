import sys

sys.stdin = open('input.txt')

from collections import deque


# T = int(input())
T = 10
for t in range(1, T+1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        # print(i)
        if lst[i+1] not in graph[lst[i]]:
            graph[lst[i]].append(lst[i+1])
#     print(graph[S])
    cnt = 0
    visited = [0] * 101
    q = deque([[S]])

    while q:
        curr = q.popleft()
#         print(curr)
        nexts = []
        for c in curr:
            for n in graph[c]:
                if not visited[n]:
                    visited[n] = 1
                    nexts.append(n)
        # print(nexts)
        if nexts:
            q.append(nexts)
        cnt = cnt + 1
    curr.sort()
    # print(curr)
    print(f'#{t} {curr[-1]}')