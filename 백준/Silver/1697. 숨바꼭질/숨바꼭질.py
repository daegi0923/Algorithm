from collections import deque


N, K = map(int, input().split())
visited = [0] * 100001
q = deque([N])
ans = 0
if N == K:
    pass
else:
    while q:
        curr = q.popleft()
        next_num = [curr + 1, curr-1, 2 * curr]
        if K in next_num:
            ans = visited[curr] + 1
            break
        for nxt in next_num:
            if 0<=nxt<=100000 and not visited[nxt]:
                q.append(nxt)
                visited[nxt] = visited[curr] + 1

print(ans)