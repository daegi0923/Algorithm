import sys

sys.stdin = open('input.txt')

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        curr = q.popleft()
        person[curr] = 1
        for adj in graph[curr]:
            if not person[adj]:
                q.append(adj)


from collections import deque
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    # print(graph)
    ans = 0
    person = [0] *(N+1)
    for idx in range(1, N+1):
        if not person[idx]:
            bfs(idx)
            ans = ans + 1
    print(f'#{t} {ans}')