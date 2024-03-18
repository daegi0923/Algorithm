import sys
sys.stdin = open('input.txt')

from collections import deque
T = int(input())
for t in range(1, T+1):
    N, S = map(int,input().split())
    cards = deque(list(range(1, N+1)))
    for _ in range(S):
        cards.rotate(N//3)
        new_cards = [0] * N
        first = 0
        second = N//2 + N%2
        idx = 0
        # print(cards)
        while True:
            # print(first, second)

            if first == N//2 + N%2:
                break
            new_cards[idx] = cards[first]
            idx = idx + 1

            if 0 <= second <N:
                new_cards[idx] = cards[second]
            first = first + 1
            second = second + 1
            idx = idx + 1
        cards = deque(new_cards)
#         print(cards)
    print(f'#{t}', *cards)
