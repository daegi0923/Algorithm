from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    cmd = list(input().split())
    if cmd[0] == 'push':
        q.append(int(cmd[1]))

    elif cmd[0] == 'pop':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)