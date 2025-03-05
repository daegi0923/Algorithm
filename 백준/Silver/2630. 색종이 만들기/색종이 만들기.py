import sys
import heapq

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0
def solve(i, j, length):
	global blue, white
	# print(i, j, length)

	if length == 1:
		if board[i][j]:
			blue = blue + 1
			# print(blue)
		else:
			white = white + 1
			# print(white)
		return
	square = [row[j:j + length] for row in board[i:i + length]]
	# print(square)
	flag = False
	color = square[0][0]
	for line in square:
		for pixel in line:
			if pixel != color:
				flag = True
				break
	if flag:
		solve(i, j, length//2)
		solve(i+length//2, j, length//2)
		solve(i, j+length//2, length//2)
		solve(i+length//2, j+length//2, length//2)
	else:
		if color:
			blue = blue + 1
			# print(blue)

		else:
			white = white + 1
			# print(white)


solve(0, 0, N)
print(white)
print(blue)
