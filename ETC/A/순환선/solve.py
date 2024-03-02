import sys
sys.stdin = open('input.txt')

def calScore(start1, end1, start2, end2):
    return (lst[start1]+lst[end1])**2 + (lst[start2]+lst[end2])**2

def dfs(n):
    global ans
    # print(used)
    if sum(used) == 4 or n == N:
        if sum(used) == 4:
            stations = [s for s in range(N) if used[s]]
            # print(stations)
            score1 = calScore(stations[0], stations[1], stations[2], stations[3])
            if score1 > ans:
                ans = score1
                # print(11, score1, used)

            score2 = calScore(stations[0], stations[3], stations[1], stations[2])
            if score2 > ans:
                ans = score2
#                 print(22, score2, used)
        return
    for i in range(n, N):
        if i == 0:
            if not used[N-1] and not used[1]:
                used[i] = 1
                dfs(i+1)
                used[i] = 0
        elif i == N-1:
            if not used[0] and not used[N-2]:
                used[i] = 1
                dfs(i+1)
                used[i] = 0
        else:
            if not used[i-1] and not used[i+1]:
                used[i] = 1
                dfs(i+1)
                used[i] = 0
            else:
                dfs(i+1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    used = [0] * N
    ans = 0
    dfs(0)
    print(f'#{t} {ans}')