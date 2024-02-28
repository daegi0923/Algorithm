import sys

sys.stdin = open('input.txt')
from queue import PriorityQueue

T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split()) # N : 맵 크기 M : 터널 개수
    map_mount = [list(map(int,input().split())) for _ in range(N)]
    relations = [[[] for _ in range(N)] for _ in range(N)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for col in range(N):
        for row in range(N):
            for i in range(4):
                tmp_col = col + dx[i]
                tmp_row = row + dy[i]
                if 0 <= tmp_col < N and 0 <= tmp_row < N:
                    if map_mount[tmp_col][tmp_row] == map_mount[col][row]: # 평지
                        dis = 1
                    elif map_mount[tmp_col][tmp_row] > map_mount[col][row]: # 오르막길
                        dis = (map_mount[tmp_col][tmp_row] - map_mount[col][row])*2
                    else: # 내리막길
                        dis = 0
                    relations[col][row].append([tmp_col,tmp_row,dis])
    for _ in range(M): # 터널 입력
        x_1,y_1,x_2,y_2,dis = map(int,input().split())
        relations[x_1-1][y_1-1].append([x_2-1,y_2-1,dis])
        relations[x_2-1][y_2-1].append([x_1-1,y_1-1,dis])

    map_visit = [[False for _ in range(N)] for _ in range(N)]
    map_dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    que = PriorityQueue()
    map_dist[0][0] = 0
    que.put([0,0,0]) # 거리,x,y 순으로 넣기
    while que.qsize():
        crt_dis,crt_col,crt_row = que.get()
        print(crt_col, crt_row)
        if crt_col == N-1 and crt_row == N-1: #도착지점이면
            [print(*row) for row in map_dist]
            print(f'#{test_case} {crt_dis}')
            break
        map_visit[crt_col][crt_row] = True # 방문처리
        for nxt_col,nxt_row,nxt_dst in relations[crt_col][crt_row]: # 다음 갈 col,row 가는데 필요한 거리(기름)
            if map_dist[nxt_col][nxt_row] > crt_dis + nxt_dst: # 지금 거리 + 가는데 필요한 거리가 해당 노드 최소 거리보다 작으면
                que.put([crt_dis+nxt_dst,nxt_col,nxt_row])
                map_dist[nxt_col][nxt_row] = crt_dis+nxt_dst
