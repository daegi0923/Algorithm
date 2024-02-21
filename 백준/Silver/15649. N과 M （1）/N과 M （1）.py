
N, M = map(int, input().split())
def dfs(i,seq, k):
    if i == k:
        print(*seq)
        return
    for num in nums:
        if not visited[num]:
            seq.append(str(num))
            visited[num] = 1
            dfs(i+1, seq, k)
            visited[num] = 0
            seq.pop()



nums = list(range(1, N+1))
visited = [0] *(N+1)
seq = []
dfs(0, seq ,M)
