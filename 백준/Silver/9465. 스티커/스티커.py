import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
	n = int(input())
	board = [list(map(int, input().split())) for _ in range(2)]
	dp = [[0] * n for _ in range(2)]
	dp[0][0] = board[0][0]
	dp[1][0] = board[1][0]
	if n == 1:
		print(max(board[0][n-1], board[1][n-1]))
		continue
	dp[0][1] = dp[1][0] + board[0][1]
	dp[1][1] = dp[0][0] + board[1][1]
	if n == 2:
		print(max(dp[0][n - 1], dp[1][n - 1]))
		continue
	for i in range(2, n):
		dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + board[0][i]
		dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + board[1][i]
	print(max(dp[0][n-1], dp[1][n-1]))
