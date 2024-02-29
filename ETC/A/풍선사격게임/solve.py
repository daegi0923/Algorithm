import sys
sys.stdin = open('input.txt')


def getMaxIdx(lst):
    if len(lst) == 1:
        return 0, lst[0]
    prohibit = lst.index(max(lst))
    max_idx = 0
    lst_max = 0
    for idx, num in enumerate(lst):
        if idx == 0:
            score = lst[1]
        elif idx == len(lst)-1:
            score = lst[len(lst)-2]
        else:
            score = lst[idx-1]*lst[idx+1]
        if score > lst_max:
            if idx != prohibit:
                max_idx = idx
                lst_max = score
    # if len(lst) == 3:

    return max_idx, lst_max
T = int(input())
for t in range(1, T+1):
    N = int(input())
    ans = 0
    lst = list(map(int, input().split()))
    while lst:
        target, score = getMaxIdx(lst)
        ans = ans + score
        print(target, score, lst, lst[target])
        lst.pop(target)
    print(f'#{t} {ans}')