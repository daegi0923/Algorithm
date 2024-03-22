import sys
sys.stdin = open('input.txt')

from collections import deque

def dfs(curr):
    visited[curr] = 1
    for next_ in graph[curr]:
        if not visited[next_]:
            dfs(next_)


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
    for curr in range(1, N+1):
        if not visited[curr]:
            dfs(curr)
            ans = ans + 1
    print(f'#{t} {ans}')