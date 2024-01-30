import sys

sys.stdin = open('input.txt')

for t in range(10):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for idx, height in enumerate(lst):
        if idx <= 2:
            near = lst[idx+1:idx+3]
        elif N-2 <= idx:
            near = lst[idx-2:idx]
        else:
            near = lst[idx-2:idx] + lst[idx+1:idx+3]
        if max(near) < height:
            cnt = cnt + (height-max(near))

    print(f'#{t+1} {cnt}')