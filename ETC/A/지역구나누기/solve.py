import sys
sys.stdin = open('input.txt')


<<<<<<< HEAD

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
=======
from collections import deque
def check(lst):
    if not lst:
        return False
    l = len(lst)
    if l == 1:
        return True
    visited = [0] * N
    start = lst[0]
    q = deque()
    q.append(start)
    while q:
        curr = q.popleft()
        visited[curr] = 1
        for i in range(N):
            if i in lst and R[curr][i] and not visited[i]:
                q.append(i)

    if sum(visited) == l:
        return True
    else:
        return False
    # for idx, num in enumerate(lst):

>>>>>>> 2e378b8bcdf2e5c9055f02ef461f71716d22207f


def dfs(n):
    global ans
    if n == N-1:
        area1 = [i for i in range(N) if used[i]]
        area2 = [i for i in range(N) if not used[i]]
        sum1 = sum(Pi[num] for num in area1)
        sum2 = sum(Pi[num] for num in area2)
<<<<<<< HEAD
        if check(area1) and check(area2) and abs(sum1-sum2) < ans:
            print(used, sum1, sum2, abs(sum1-sum2))
=======
        # print(area1, area2, check(area1), check(area2))
        if check(area1) and check(area2) and abs(sum1-sum2) < ans:
#             print(used, sum1, sum2, abs(sum1-sum2))
>>>>>>> 2e378b8bcdf2e5c9055f02ef461f71716d22207f
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

