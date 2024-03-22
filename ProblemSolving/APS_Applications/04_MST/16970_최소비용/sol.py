import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    distance = [[float('inf')] * N for _ in range(N)]

    direct = (0, 1), (1, 0), (-1, 0), (0, -1)

    queue = []
    heappush(queue, (0, 0, 0))
    distance[0][0] = 0

    while queue:
        dist, x, y = heappop(queue)
        for dir in direct:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[x][y]-graph[nx][ny] >= 0:
                    new_dist = dist + 1
                else:
                    new_dist = dist + 1 + abs(graph[x][y]-graph[nx][ny])

                if new_dist >= distance[nx][ny]:
                    continue

                distance[nx][ny] = new_dist
                heappush(queue, (new_dist, nx, ny))

    print(f'#{test_case} {distance[N-1][N-1]}')