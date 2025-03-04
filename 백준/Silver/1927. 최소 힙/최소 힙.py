import sys
import heapq

input = sys.stdin.readline


hq = []
N = int(input())
for _ in range(N):
	x = int(input())
	if x == 0:
		if hq:
			print(heapq.heappop(hq))
		else:
			print(0)
	else:
		heapq.heappush(hq, x)

