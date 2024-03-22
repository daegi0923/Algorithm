import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    form = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for i in range(0, 2*M, 2):
        graph[form[i]].append(form[i+1])
        graph[form[i+1]].append(form[i])
    visited = [0] * (N+1)
    ans = 0
    for start in range(1, N+1):
        if not visited[start]:
            q = deque([start])
            while q:
                curr = q.popleft()
                visited[curr] = 1
                # print(curr)
                for next_ in graph[curr]:
                    if not visited[next_]:
                        q.append(next_)
            ans = ans + 1
    print(f'#{t} {ans}')

    # print(graph)