from collections import deque

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0] * (n+1)
q = deque([p1])
ans = -1
visited[p1] = 1
if p1 == p2:
    ans = 0
else:
    while q:
        curr = q.popleft()
        nxts = graph[curr]
        if p2 in nxts:
            ans = visited[curr]
            break
        for nxt in nxts:
            if not visited[nxt]:
                visited[nxt] = visited[curr] + 1
                q.append(nxt)
# print(graph)
# print(visited)
print(ans)