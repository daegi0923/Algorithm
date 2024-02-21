import sys


sys.stdin = open('input.txt')
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1} # 스택 밖에서의 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1} # 스택 안에서의 우선순위
T = 10
for t in range(T):
    N = int(input())
    line = input()
    stack = []
    cal = ""
    for tk in line:
        # 여는 괄호 push, 연산자이고 top 원소보다 우선순위가 높으면 push
        if not stack and tk in '*+-/':
            stack.append(tk)
        elif tk == '(' or (tk in '*/+-' and isp[stack[-1]] < isp[tk]):
            stack.append(tk)
        elif tk in '*/+-' and isp[stack[-1]] >= isp[tk]:  # 연산자이고 top 원소보다 우선순위가 높지 않으면
            # top 원소의 우선순위가 낮을 때까지 pop
            while stack and isp[stack[-1]] >= isp[tk]:
                cal = cal + stack.pop()

            # push
            stack.append(tk)

        elif tk == ')':  # 닫는 괄호면, 여는 괄호를 만날 때 까지 pop
            while stack and stack[-1] != '(':
                cal = cal + stack.pop()
            stack.pop()  # 여는 괄호 pop해서 버려
        else:  # 피연산자인 경우
            cal = cal + tk
    else:
        while stack:
            cal = cal + stack.pop()
    print(cal)
    stack = []
    for tk in cal:
        if tk in icp:
            num1 = stack.pop()
            num2 = stack.pop()
            if tk == '+':
                stack.append(num1 + num2)
            if tk == '*':
                stack.append(num1 * num2)
            if tk == '-':
                stack.append(num1 - num2)
            if tk == '/':
                stack.append(num1 // num2)

        else:
            stack.append(int(tk))
    print(f'#{t+1} {stack[-1]}')