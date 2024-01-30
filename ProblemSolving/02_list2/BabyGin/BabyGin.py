import sys


sys.stdin = open("input.txt")
T = int(input())
for t in range(T):
    num = int(input())
    cards = []
    for i in range(6):
        cards.append(num%10)
        num = num//10
    cnts = [cards.count(i) for i in range(11)]
    print(cnts)
    for idx, cnt in enumerate(cnts):
        if cnt >= 3:
            cnts[idx] = cnts[idx] - 3 * (cnt // 3)

        if idx < 7 and cnt > 0 and cnts[idx] == cnts[idx + 1] == cnts[idx + 2] > 0:
            num_run = cnts[idx]
            cnts[idx] = cnts[idx] - num_run
            cnts[idx + 1] = cnts[idx + 1] - num_run
            cnts[idx + 2] = cnts[idx + 2] - num_run
    print(cnts)

    if cnts.count(0) == len(cnts):
        ans = 'true'
    else:
        ans = 'false'
    print(f'#{t + 1} {ans}')