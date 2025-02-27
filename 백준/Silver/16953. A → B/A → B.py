import sys
from collections import deque
input = sys.stdin.readline


A, B = map(int, input().split())
dp = dict()
dp[A] = 1
queue = deque([[A]])
ans = 1
while queue:
	curr = queue.popleft()
	nextNums = []
	for num in curr:
		# print(num, curr)
		if num == B:
			break
		if num*2 <= B and num*2 not in dp:
			dp[num*2] = ans + 1
			nextNums.append(num*2)
		if num * 10 + 1 <= B and num*10+1 not in dp:
			dp[num * 10 + 1] = ans + 1
			nextNums.append(num * 10 + 1)

	if nextNums:
		queue.append(nextNums)
		ans = ans + 1
if B in dp:
	print(dp[B])
else:
	print(-1)