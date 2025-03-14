import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# O는 빈 공간, X는 벽, I는 도연이, P는 사람

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

si = [1 for line in board if 'I' in line][0]
sj = [line.index('I') for line in board if 'I' in line][0]
visited[si][sj] = 1
q = deque([(si, sj)])
ans = 0
while q:
	ci, cj = q.popleft()
	if board[ci][cj] == 'P':
		ans = ans + 1
	for d in range(4):
		nextI = ci + di[d]
		nextJ = cj + dj[d]
		if nextI < 0 or N <= nextI or nextJ < 0 or M <= nextJ:
			continue
		if not visited[nextI][nextJ] and board[nextI][nextJ] != 'X':
			visited[nextI][nextJ] = 1
			q.append((nextI, nextJ))
if ans:
	print(ans)
else:
	print('TT')