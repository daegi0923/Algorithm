import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    words = [input() for _ in range(5)]
    ans = ''
    i = 0
    max_len = max([len(word) for word in words])
    for i in range(max_len):
        for word in words:
            if i<len(word):
                ans = ans + word[i]
    print(f'#{t+1} {ans}')