import sys
sys.stdin = open('input.txt')

def bfs(start):
    global result
    visited = [0] * 1000001
    cnt = 0
    points = [start]
    while True:
        lstlst = []
        for c in points:
            for n in [c+1, c-1, c*2, c-10]:
                if 1000000 >= n > 0 and visited[n] == 0:
                    visited[n] = 1
                    lstlst.append(n)
        cnt += 1
        if M in lstlst:
            result = min(cnt, result)
            return
        points = lstlst

T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    result = 9999

    bfs(N)

    print(f'#{test_case} {result}')