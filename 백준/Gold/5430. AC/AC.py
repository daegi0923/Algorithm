from collections import deque


T = int(input())
for _ in range(T):

    p = list(input())
    n = int(input())
    lst = input()
    if n > 0:
        lst = list(lst.strip('[').strip(']').split(','))
        deq = deque(lst)
    else:
        deq = deque()
    flag = 0
    side = 0 # 0 : left, 1 : right
    for cmd in p:
        if cmd == "R":
            side = (side + 1) % 2
        if cmd == "D":
            if len(deq) == 0:
                print('error')
                flag = 1
                break
            if side == 0:
                deq.popleft()
            else:
                deq.pop()

    if side == 1:
        deq.reverse()
    if flag == 0:
        print('['+','.join(deq)+']')