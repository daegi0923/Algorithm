import sys


sys.stdin = open('input.txt')

T = int(input())
o_bras = ['(', '{', '[']
c_bras = [')', '}', ']']
bras = {'(':')', '{': '}', '[':']'}
for t in range(T):
    line = input()
    stack = []
    for c in line:
        if c in o_bras:
            stack.append(c)
        if c in c_bras:
            if stack and o_bras.index(stack[-1]) == c_bras.index(c):
                stack.pop()
            else:
                ans = 0
                break
    else:
        if stack:
            ans = 0
        else:
            ans = 1
    print(f'#{t+1} {ans}')