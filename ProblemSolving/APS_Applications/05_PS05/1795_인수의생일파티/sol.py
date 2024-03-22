import sys

sys.stdin = open('input.txt')



T = int(input())
for t in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = [[float('inf')] *(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x][y]=c
    for i in range(N+1):
        graph[i][i] = 0
    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+ graph[k][j])
    # print(graph)
    ans = 0


    print(f'#{t} {ans}')