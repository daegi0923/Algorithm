import sys

input = sys.stdin.readline


N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst = sorted(list(set(lst)))
res = []
def solve(start, res):
	if len(res) == M:
		print(*res)
		return
	for i in range(start, len(lst)):
			solve(i, res + [lst[i]])

solve(0, [])
