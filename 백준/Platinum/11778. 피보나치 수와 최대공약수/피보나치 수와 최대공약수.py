import math
mod = 10**9+7

memo = {1:1,2:1,3:2,4:3,5:5}

def Fibo(n):
  if memo.get(n):
    return memo[n]
  else:
    if n%2 == 1:
      memo[n] = (Fibo(n//2)**2+Fibo(n//2+1)**2)%mod
    else:
      memo[n] = (Fibo(n+1)-Fibo(n-1))%mod
    return memo[n]

N,M = map(int,input().split())
print(Fibo(math.gcd(N,M)))