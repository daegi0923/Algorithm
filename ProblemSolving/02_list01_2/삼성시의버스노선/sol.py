import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    stop_num = [0] * 5001

    for i in range(N):
        a, b = map(int, input().split())
        for num in range(a, b+1):
            stop_num[num] = stop_num[num] + 1

    P = int(input())
    ans = [stop_num[int(input())] for _ in range(P)]
    print(f"#{t+1}", *ans)
