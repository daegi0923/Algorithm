import sys
sys.stdin = open('input.txt')


from collections import deque


T = int(input())
for t in range(1,T+1):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):

        start, end = map(int,input().split())
        # print(s, e)
        graph[start].append(end)
        graph[end].append(start)

    S, G = map(int,input().split())
    q = deque([S])
    visited = {S : 0}
    # print(graph)

    while q:
        curr = q[0]
        q.popleft()
        if graph[curr]:
            for next_ in graph[curr]:
                if next_ not in visited:
                    q.append(next_)
                    visited[next_] = visited[curr]+1
        if curr == G:
            break
    print(f'#{t} {visited.get(G, 0)}')