import heapq


N = int(input())
cards = list(int(input()) for _ in range(N))
heapq.heapify(cards)
ans = 0

while len(cards) != 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    res = first + second
    ans += res
    heapq.heappush(cards, res)

print(ans)