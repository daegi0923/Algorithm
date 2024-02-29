import sys
sys.stdin = open('input.txt')



def check(lst):
    if len(lst) == 1:
        return True
    accessible = [0] * N
    for i in lst:
        for town in range(N):
            if R[i][town]:
                accessible[town] = 1
    check_town = [accessible[town] for town in lst]
    if sum(check_town) == len(lst):
        return True
    else:
        return False


def dfs(n):
    global ans
    if n == N-1:
        area1 = [i for i in range(N) if used[i]]
        area2 = [i for i in range(N) if not used[i]]
        sum1 = sum(Pi[num] for num in area1)
        sum2 = sum(Pi[num] for num in area2)
        if check(area1) and check(area2) and abs(sum1-sum2) < ans:
            print(used, sum1, sum2, abs(sum1-sum2))
            ans = abs(sum1-sum2)
        return
    used[n] = 1
    dfs(n+1)
    used[n]= 0
    dfs(n+1)




T = int(input())
for t in range(1, T+1):
    N = int(input())
    R = [list(map(int, input().split())) for _ in range(N)]
    Pi = list(map(int,input().split()))
    tot = sum(Pi)
    used = [0] * N
    ans = float('inf')
    # print(used)
    dfs(0)
    print(f'#{t} {ans}')

