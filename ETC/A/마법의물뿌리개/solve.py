import sys


sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_tree = max(trees)
    diff_list = [max_tree - trees[i] for i in range(N)]
    # print(diff_list)
    singles = 0
    doubles = 0
    for idx, diff in enumerate(diff_list):
        singles = singles  + diff%2
        doubles = doubles + diff//2
    ans = 0
    while True:
        if not singles and not doubles:
            break
        ans = ans + 1
        if ans%2 and singles:
            singles = singles - 1
        elif ans%2 and not singles:
            if doubles > 1:
                doubles = doubles - 1
                singles = singles + 1
        elif not ans%2 and doubles:
            doubles = doubles - 1
    print(f'#{t} {ans}')
