import sys

input = sys.stdin.readline
N = int(input())
lst = [0]*N
dp = [0]*N
for i in range(N):
	lst[i] = int(input())
for i in range(N):
	if i == 0:
		dp[i] = lst[i]
	elif i == 1:
		dp[i] = lst[i-1] + lst[i]
	elif i == 2:
		dp[i] = max(lst[i-2] + lst[i], lst[i-1]+lst[i])
	else:
		dp[i] = max(dp[i-2]+lst[i], dp[i-3]+lst[i-1]+lst[i])
print(dp[N-1])
