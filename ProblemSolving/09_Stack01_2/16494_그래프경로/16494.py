import sys

sys.stdin =  open('input.txt')

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    graph = [[]for _ in range(V+1)]
    visited = [0] * (V+1) # 0 : not visited, 1 : visited
    result = 0
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
    S, G = map(int, input().split())
    stack = [S]
    while stack:
        if graph[stack[-1]]:
            curr = stack[-1]
            for next_ in graph[curr]:
                if visited[next_] == 0:
                    stack.append(next_)
                    visited[next_] = 1
                    break
            else:
                stack.pop()
        else:
            stack.pop()
        if next_ == G:
            result = 1
            break
    print(f'#{t+1} {result}')
