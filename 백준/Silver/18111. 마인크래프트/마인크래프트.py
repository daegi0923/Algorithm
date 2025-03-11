import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
# print(board)
min_time = float('inf')
best_height = 0
target = 0
for target in range(257):
	increase = 0
	decrease = 0

	for i in range(N):
		for j in range(M):
			height = board[i][j]
			if height < target:
				increase = increase + (target - height)
			else:
				decrease = decrease + (height - target)

	if decrease + B >= increase:
		time = (decrease * 2) + increase
		if time < min_time or (time == min_time and target > best_height):
			min_time = time
			best_height = target

print(min_time, best_height)