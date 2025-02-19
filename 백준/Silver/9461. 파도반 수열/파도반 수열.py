import sys

input = sys.stdin.readline
T = int(input())
dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90
# print(dp)
for i in range(101):
	if i > 10:
		dp[i] = dp[i-1] + dp[i-5]
for _ in range(T):
	N = int(input())
	print(dp[N])
