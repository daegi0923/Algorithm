def dfs(curr,length):
    if length == M:
        print(*stack)
        return
    for num in range(curr, N+1):
        stack.append(num)
        dfs(num, length+1)
        stack.pop()


N, M = map(int, input().split())
stack = []
dfs(1, 0)