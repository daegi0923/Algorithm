import heapq

N, K = map(int, input().split())
lst = [0] * 100001
lst[N] = 1
hq = [[0, N]]
while hq:
    curr = heapq.heappop(hq)
    lst[curr[1]] = curr[0]
    if curr[1] == K:
        break
    c = curr[1]
    if 0<= c-1 and not lst[c-1]:
        heapq.heappush(hq, [curr[0]+1, c-1])
    if c+1 < 100001 and not lst[c+1]:
        heapq.heappush(hq, [curr[0]+1, c+1])
    if c!= 0 and 2*c < 100001 and not lst[2*c]:
        heapq.heappush(hq, [curr[0], 2*c])
print(lst[K])