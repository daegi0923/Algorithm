N = int(input())

matrix = [[0]*1001 for _ in range(1001)]
for n in range(N):
    x, y, width,height = list(map(int, input().split()))
    for i in range(x, max(x, x+width)):
        for j in range(y, max(y, y+height)):
            matrix[i][j] = n+1
for n in range(N):
    print(sum([row.count(n+1) for row in matrix]))
    