import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    start = N//2 + N%2
    second = cards[start:]
    cards = deque(cards)
    second = deque(second)
    ans = deque()
    for idx in range(N):
        if idx%2 and second:
            ans.append(second.popleft())
        else:
            ans.append(cards.popleft())




    print(f'#{t}', *ans)