import sys


sys.stdin = open('input.txt')
T = int(input())

for t in range(T):
    stack = []
    line = input().strip().split()
    ans = 'error'
    for tk in line:
        if tk in '/*+-':
            if len(stack) >= 2:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if tk == '+':
                    stack.append(num1 + num2)
                elif tk == '-':
                    stack.append(num1 - num2)
                elif tk == '*':
                    stack.append(num1 * num2)
                elif tk == '/':
                    if num2 == 0:
                        break
                    stack.append(num1 // num2)
            else:
                break
        elif tk == '.':
            if len(stack) == 1:
                ans = stack[0]
            else:
                break
        else:
            stack.append(int(tk))

    print(f'#{t+1} {ans}')
