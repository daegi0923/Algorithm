import sys

def game(first, second):
    global cards
    if cards[first] - cards[second] == 0:
        return first
    elif abs(cards[first]-cards[second]) == 1:
        if cards[first] > cards[second]:
            return first
        else:
            return second
    else:
        if cards[first]>cards[second]:
            return second
        else:
            return first


def partition(left, right):
    if left == right:
        return left
    else:
        return game(partition(left, (right+left)//2), partition((right+left)//2+1, right))




sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N = int(input())
    cnt = 0
    cards = list(map(int, input().split()))

    ans = partition(0, N-1)
    print(f'#{t+1} {ans+1}')
