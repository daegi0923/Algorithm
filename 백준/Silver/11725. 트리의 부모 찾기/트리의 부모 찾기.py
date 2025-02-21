import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tree = {i:[] for i in range(1, N+1)}
parents = [0] * (N+1)
parents[1] = 1
for _ in range(N-1):
	s, e = map(int, input().split())
	tree[s].append(e)
	tree[e].append(s)
# print(tree)

queue = deque([1])
while queue:
	curr = queue.popleft()
	# print(curr)
	# print(tree[curr])
	for nextNode in tree[curr]:
		if not parents[nextNode]:
			parents[nextNode] = curr
			queue.append(nextNode)
[print(parent) for parent in parents[2:]]