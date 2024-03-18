import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    num = int(input())
    lst = [0] * 5
    divs = [2, 3, 5, 7, 11]
    idx = 0
    while True:
        if num % divs[idx] == 0:
            lst[idx] = lst[idx] + 1
            num = num/divs[idx]
        else:
            idx = idx + 1
        if idx > len(lst)-1:
            break
    print(f'#{t+1}', *lst)