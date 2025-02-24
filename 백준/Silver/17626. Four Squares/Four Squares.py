import sys
import math
input = sys.stdin.readline

n = int(input())

dp = [0] * 50001
dp[1] = 1
squares = [1]
for i in range(2, n+1):
	sqrt = math.sqrt(i)
	if sqrt-math.floor(sqrt) == 0:
		squares.append(i)
		dp[i] = 1
	else:
		dp[i] = min([dp[i-square]+1 for square in squares])
print(dp[n])