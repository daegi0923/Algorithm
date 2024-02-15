import sys
from collections import deque


sys.stdin = open('input.txt')
for _ in range(10):
    t = int(input())
    pw = deque(list(map(int, input().split())))
    while True:
        if pw[-1] == 0:
            break
        for cycle in range(1, 6):
            pw.rotate(-1)
            pw[-1] = max(pw[-1] - cycle, 0)
            if pw[-1] == 0:
                break
        else:
            cycle = cycle + 1

    print(f'#{t}', *pw)
