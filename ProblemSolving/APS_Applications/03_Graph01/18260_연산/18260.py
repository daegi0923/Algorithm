import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    ans = float('inf')
    curr = [N]
    visited[N] = 1
    cnt = 0
    while True:
        nexts = []
        for c in curr:
            for n in [c+1, c*2, c-1, c-10]:
                if 0< n <= 1000000 and not visited[n]:
                    nexts.append(n)
                    visited[n] = 1
            # nexts.extend(list(filter(lambda x: 0<= x <= 1000000 and not visited[x], [n+1, n*2, n-1, n-10])))
        cnt = cnt + 1
        if M in nexts:
            break
        curr = nexts



    print(f'#{t} {cnt}')