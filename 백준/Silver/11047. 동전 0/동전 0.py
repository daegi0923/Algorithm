N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
ans = 0
while True:
    if K <= 0:
        break
    if K // A[N-1] >= 1:
        ans = ans + K//A[N-1]
        K =  K - K//A[N-1] * A[N-1]
    N = N - 1
print(ans)