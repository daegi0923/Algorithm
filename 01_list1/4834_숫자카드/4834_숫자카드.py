import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    cards = list(map(int, input()))
    # print(cards)
    cnts = [cards.count(idx) for idx in range(10)]
    # print(cnts)
    max_cnt = cnts[0]
    max_idx = 0
    for idx, cnt in enumerate(cnts):
        if max_cnt <= cnt:
            max_cnt = cnt
            max_idx = idx

    print(f'#{t+1} {max_idx} {max_cnt}')
