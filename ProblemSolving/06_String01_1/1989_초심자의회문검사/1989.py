import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    word = input()
    if word == word[::-1]:
        print(f'#{t+1}', 1)
    else:
        print(f'#{t+1}',0)