import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
M = int(input())
graph = {i:[] for i in range(1, N+1)}
# print(graph)
visited = [0] * (N+1)
for _ in range(M):
	start, end = map(int, input().split())
	# print(start, end)
	graph.get(start).append(end)
	graph.get(end).append(start)
# print(graph)

def bfs():
	queue = deque()
	queue.append(1)
	while queue:
		# print(queue)
		curr = queue.popleft()
		if not visited[curr]:
			visited[curr]=1
		for nxt in graph.get(curr):
			# print(nxt)
			if not visited[nxt]:
				visited[nxt] = 1
				queue.append(nxt)

bfs();
# print(visited)
print(sum(visited)-1)