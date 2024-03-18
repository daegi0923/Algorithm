import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    ans = 0
    for i in range(-N, N+1):
        for j in range(-N, N+1):
            if i**2 + j**2 <= N**2:
                ans = ans + 1
    print(f"#{t+1} {ans}")