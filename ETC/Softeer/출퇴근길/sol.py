import sys
sys.stdin = open('input.txt')

def dfs(curr, e, direction, visited):
    if curr == e:
        return
    for nxt in direction[curr]:
        if not visited[nxt]:
            visited[nxt] = 1
            dfs(nxt, e, direction, visited)


    return
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
r_graph = [[] for _ in range(n+1)]
for _ in range(m):
    xi, yi = map(int, input().split())
    graph[xi].append(yi)
    r_graph[yi].append(xi)
S, T = map(int, input().split())
ans = 0
for idx in range(n):
    StoX = [0] * (n+1)
    XtoT = [0] * (n+1)
    TtoX = [0] * (n+1)
    XtoS = [0] * (n+1)
    dfs(S, idx, graph, StoX)
    dfs(idx,S, r_graph, XtoS)
    dfs(T, idx, graph, TtoX)
    dfs(idx, T,r_graph, XtoT)
    if 
print(graph)
print(r_graph)


