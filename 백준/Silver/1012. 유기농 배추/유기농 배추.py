import sys
from collections import deque

input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(board, sx, sy):
	global ans
	queue = deque([(sx, sy)])
	while queue:
		x, y = queue.popleft()
		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]
			if nx < 0 or nx >= M or ny < 0 or ny >= N:
				continue
			if board[ny][nx] == 1:
				board[ny][nx] = -1
				queue.append((nx, ny))
	ans = ans + 1
T = int(input())

for _ in range(T):

	M, N, K = map(int, input().split())
	board = [[0] * M for _ in range(N)]
	for _ in range(K):
		x, y = map(int, input().split())
		board[y][x] = 1
	# [print(line) for line in board]
	ans = 0
	for i in range(M):
		for j in range(N):
			if board[j][i] == 1:
				bfs(board, i, j)
	print(ans)
