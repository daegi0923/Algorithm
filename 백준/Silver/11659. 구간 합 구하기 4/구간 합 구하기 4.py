import sys

input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst = [0] + lst
prefix = [0] * (N+1)
curr = 0
for i in range(1, N+1):
	curr = curr + lst[i]
	prefix[i] = curr
for _ in range(M):
	i, j = map(int, input().split())
	ans = prefix[j] - prefix[i-1]
	print(ans)