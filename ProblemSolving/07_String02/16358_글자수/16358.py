import sys

sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    str1 = input()
    str2 = input()
    ans = 0
    for c in str1:
        cnt = str2.count(c)
        if ans < cnt:
            ans = cnt
    print(f'#{t+1} {ans}')