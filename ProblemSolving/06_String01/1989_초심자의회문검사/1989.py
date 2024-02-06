import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    ans = 0
    word = input()
    if word == word[::-1]:
        ans = 1
    else:
        ans = 0
    print(f'#{t+1} {ans}')