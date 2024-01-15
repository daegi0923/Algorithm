matrix = [[0] * 100 for _ in range(100+1)]
for _ in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))

    for i in range(x1, x2):
        for j in range(y1, y2):

            matrix[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        ans += matrix[i][j]
print(ans)