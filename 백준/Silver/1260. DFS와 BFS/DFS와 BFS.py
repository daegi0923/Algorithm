import sys
from collections import deque

input = sys.stdin.readline


N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
	s, e = map(int, input().split())
	graph[s][e] = 1
	graph[e][s] = 1
visited = [0] * (N+1)
visited[V] = 1
trace = [V]
def dfs(start):
	global visited
	for i in range(1, N+1):
		if graph[start][i] == 1 and not visited[i]:
			visited[i] = 1
			trace.append(i)
			dfs(i)
	return
dfs(V)
print(*trace)
def bfs(start):
	queue = deque([V])
	bfsVisited = [0] * (N+1)
	bfsVisited[V] = 1
	trace = [V]
	while queue:
		curr = queue.popleft()
		for i in range(1, N+1):
			if graph[curr][i] == 1 and not bfsVisited[i]:
				queue.append(i)
				trace.append(i)
				bfsVisited[i] = 1

	return trace

bfsTrace = bfs(V)
print(*bfsTrace)