N, M = map(int,input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
ans = 0
sharks = []
for i in range(N):
	for j in range(M):
		if matrix[i][j] == 1:
			sharks.append((i, j))
for i in range(N):
	for j in range(M):
		if matrix[i][j] != 1:
			local_min = float('inf')
			for s in sharks:
				si, sj = s
				local_ans = max(abs(si-i),abs(sj-j))
				if local_min > local_ans:
					local_min = local_ans
			if ans < local_min:
				ans = local_min
print(ans)
