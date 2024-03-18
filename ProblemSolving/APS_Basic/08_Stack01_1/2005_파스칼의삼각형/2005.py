def triangle(n):
    global tri
    if n >= 2:
        tri[1] = [1, 1]
        for i in range(2, n):
            if tri[i] == 0:
                tri[i] = [tri[i-1][j-1]+tri[i-1][j] for j in range(1, i)]
                tri[i] = [1] + tri[i] + [1]


T = int(input())
tri = [0] * 10
tri[0] = [1]
for t in range(T):
    N = int(input())
    triangle(N)
    print(f'#{t+1}')
    [print(*line) for line in tri[:N]]
