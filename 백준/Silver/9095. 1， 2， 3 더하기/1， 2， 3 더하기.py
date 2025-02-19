import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
dp = [0] * 12
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
for idx, el in enumerate(dp):
	if idx <=3:
		continue
	else:
		dp[idx] = dp[idx-1] + dp[idx-2] + dp[idx-3]


for _ in range(T):
	n = int(input())
	print(dp[n])