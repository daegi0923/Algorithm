import sys

input = sys.stdin.readline
N = int(input())

dp = [0] * (N + 1)  # 필요 없는 메모리 낭비 방지
if N >= 2:
    dp[2] = 1
if N >= 3:
    dp[3] = 1

for i in range(4, N + 1):
    lst = [dp[i - 1]]
    if i % 2 == 0:
        lst.append(dp[i // 2])
    if i % 3 == 0:
        lst.append(dp[i // 3])
    dp[i] = min(lst) + 1

print(dp[N])
