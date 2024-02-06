import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    A, B = input().split()
    N = len(A)
    M = len(B)
    cnt = 0
    while True:
        if B not in A:
            result = len(A)
            break
        A = A.replace(B,'*')

    ans = N - (M-1)*cnt
    print(f'#{t+1} {result}')