import sys

input = sys.stdin.readline
N = int(input())
pi = list(map(int, input().split()))
ans = 0
pi.sort()
for idx, el in enumerate(pi):
	#print(idx, el)
	ans = ans + (N-idx)*el
print(ans)