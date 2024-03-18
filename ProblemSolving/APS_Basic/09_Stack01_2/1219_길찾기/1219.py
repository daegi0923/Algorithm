import sys

sys.stdin =  open('input.txt')
for _ in range(10):
    T, N = map(int,input().split())
    lst = list(map(int,input().split()))
    path1 = [0] * 100
    path2 = [0] * 100
    for n in range(N):
        s, e = lst[2*n:2*n+2]
        if path1[s] == 0:
            path1[s] = e
        else:
            path2[s] = e
    stack_node = [0]
    stack_path = [0]
    result = 0
    while stack_node:
        curr = stack_node[-1]
        if stack_path[-1] == 0 and path1[curr] != 0:
            next_ = path1[curr]
            stack_path[-1] = 1
            stack_path.append(0)
            stack_node.append(next_)
        elif stack_path[-1] == 1 and path2[curr] != 0:
            next_ = path2[curr]
            stack_path[-1] = 2
            stack_path.append(0)
            stack_node.append(next_)
        else:
            stack_node.pop()
            stack_path.pop()
        if next_ == 99:
            result = 1
            break
    print(f'#{T} {result}')