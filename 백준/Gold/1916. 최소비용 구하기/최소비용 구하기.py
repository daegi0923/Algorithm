import sys
import heapq


input = sys.stdin.readline

N = int(input())
M = int(input())
graph = {i:[] for i in range(N+1)}
costs = [float('inf')] * (N+1)

for _ in range(M):
	s, e, cost  = map(int, input().split())
	graph[s].append({'to' : e, 'cost' : cost})

# print(graph)
start, end = map(int, input().split())
def dijkstra(start, end):
	hq = [(0, start)]
	costs[start] = 0
	while hq:
		currCost, currNode = heapq.heappop(hq)
		# print(currCost, currNode)
		# print(graph[currNode])
		if not graph[currNode]:
			continue
		if currCost > costs[currNode]:
			continue
		for nxt in graph[currNode]:
			nextCost = nxt['cost']
			nextNode = nxt['to']
			# print('next', nextCost, nextNode)

			if currCost + nextCost < costs[nextNode]:
				heapq.heappush(hq, (currCost+nextCost, nextNode))
				costs[nextNode] = currCost + nextCost

	return costs[end]

ans = dijkstra(start, end)
# print(costs)
print(ans)