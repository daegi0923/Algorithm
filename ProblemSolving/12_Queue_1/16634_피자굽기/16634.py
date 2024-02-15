import sys

sys.stdin = open('input.txt')

from collections import deque


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    queue = deque()
    [queue.append([idx, cheese]) for idx, cheese in enumerate(pizzas[:N])]
    idx = N
    while True:
        if len(queue) == 1:
            break
        if queue[0][1] == 0:
            if idx <= M-1:
                queue[0] = [idx, pizzas[idx]]
                idx = idx + 1
            else:
                while queue[0][1] == 0:
                    if len(queue) == 1:
                        break
                    queue.popleft()

        queue[0][1] = queue[0][1] //2
        queue.rotate(-1)
    print(f'#{t} {queue[0][0]+1}')