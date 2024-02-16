import sys

sys.stdin = open('input.txt')

from collections import deque



T = 10
for t in range(1, T+1):
    N, start = map(int, input().split())
    graph = [[] for _ in range(101)]
    visited = []
    q = deque([start])
    lst = list(map(int, input().split()))
    for n in range(N//2):
        graph[lst[2*n]].append(lst[2*n+1])
    depth = {start: 0}
    while q:
        curr = q[0]
        visited.append(curr)
        q.popleft()
        if graph[curr]:
            for n in graph[curr]:
                if n not in visited:
                    q.append(n)
                    if n not in depth:
                        depth[n] = depth[curr]+1
    visited.sort()
    visited.sort(key=depth.get)
    print(f'#{t} {visited[-1]}')