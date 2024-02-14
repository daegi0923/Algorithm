import sys


sys.stdin = open('input.txt')

for t in range(10):
    N, pw = input().split()
    stack = []
    for c in pw:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    ans = ''.join(stack)
    print(f'#{t+1} {ans}')