import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]


for i in range(n):
	graph[i] = list(map(int, input().split())) + [0]*(n-i-1)

dp = [[0] * n for _ in range(n)]
for i in range(n-1, -1, -1):
	if i == n-1:
		dp[i] = graph[i]
		continue
	for j in range(n):
		if j <= i:
			dp[i][j] = max(dp[i+1][j],dp[i+1][j+1]) + graph[i][j]

print(dp[0][0])