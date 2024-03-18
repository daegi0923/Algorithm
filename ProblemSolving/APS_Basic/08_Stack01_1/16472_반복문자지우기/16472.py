import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    word = list(input())
    stack = []
    while True:
        if len(word) == 0:
            break
        stack.append(word[-1])
        word.pop()
        # print(word, stack)
        while len(word)>0 and len(stack)>0:
            if word[-1] != stack[-1]:
                break
            else:
                word.pop()
                stack.pop()
    print(f'#{t+1} {len(stack)}')