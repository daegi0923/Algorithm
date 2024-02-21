import sys


sys.stdin = open('input.txt')
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1} # 스택 밖에서의 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1} # 스택 안에서의 우선순위
T = 10
for t in range(T):
    N = int(input())
    line = input()
    stack = [0] * N
    top = -1
    cal = ""
    for tk in line:
        if tk == '(' or (tk in isp and top >= 0 and isp[stack[top]] < isp[tk]) or (tk in isp and top == -1):
            top = top + 1
            stack[top] = tk
        elif tk in isp and top >= 0 and isp[stack[top]] >= isp[tk]:
            while top > -1 and isp[stack[top]] >= isp[tk]:
                top = top - 1
                cal = cal + tk
            top = top + 1
            stack[top] = tk
        else:
            cal = cal + tk
    else:
        cal = cal + stack[top]
        top = top - 1

    # print(cal)
    stack = []
    for tk in cal:
        if tk in icp:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(num1 + num2)
        else:
            stack.append(tk)
    print(f'#{t+1} {stack[-1]}')


