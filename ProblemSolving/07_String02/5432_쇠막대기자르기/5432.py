import sys

sys.stdin = open('input.txt')
T = int(input())
lst = []

for t in range(T):
    ans = 0
    bars = input()
    for idx, c in enumerate(bars):
        if c == '(':
            if bars[idx+1] == ')':
                # lst 안비어있으면 +1 씩 더해줌
                if len(lst) > 0:
                    for idx in range(len(lst)):
                        lst[idx] = lst[idx] + 1
            else:
                lst.append(0)
        else:
            if bars[idx-1] == '(':
                continue
            else:
                ans = ans + lst[-1] + 1
                lst.pop()
    print(f'#{t+1} {ans}')