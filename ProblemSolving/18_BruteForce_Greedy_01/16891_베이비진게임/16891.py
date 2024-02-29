import sys
sys.stdin = open('input.txt')
from collections import deque
T = int(input())
def checkBabygin(lst):
    check = 0
    if len(lst)<3:
        return check
    for num in lst:
        if num+1 in lst and num+2 in lst:
            check = 1
            return check
        if lst.count(num) >=3:
            check = 1
            return check


for t in range(1, T+1):
    cards = list(map(int,input().split()))
    cards = deque(cards)
    player1 = []
    player2 = []
    ans = 0
    while cards:
        player1.append(cards.popleft())
        if checkBabygin(player1):
            ans = 1
            break
        player2.append(cards.popleft())
        if checkBabygin(player2):
            ans = 2
            break
    print(f'#{t} {ans}')