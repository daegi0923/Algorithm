import sys


sys.stdin = open('input.txt')


T = int(input())
for t in range(T):
    path = [0] * 200
    N = int(input())
    for _ in range(N):
        start, end = map(int, input().split())
        start, end = (start - 1)//2, (end-1)//2
        if start > end:
            start, end = end, start
        for idx in range(start, end+1):
            path[idx] = path[idx] + 1
    print(f'#{t+1} {max(path)}')
