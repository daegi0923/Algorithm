import sys

sys.stdin = open('input.txt')

def calDistance(starti, startj, endi, endj):
    return abs(starti-endi) + abs(startj - endj)



def dfs(ci, cj, n, local_sum):
    global ans
    if n ==  N:
        if local_sum + calDistance(ci, cj, ei, ej) < ans:
            ans = local_sum + calDistance(ci, cj, ei, ej)
            return
    for loc_num, loc in enumerate(locations):
        ni, nj = loc
        next_distance =calDistance(ci, cj, ni, nj)
        if not visited[loc_num] and local_sum + next_distance + calDistance(ni, nj, ei, ej)< ans:
            visited[loc_num] = 1
            dfs(ni, nj, n+1, local_sum + next_distance)
            visited[loc_num] = 0

T = int(input())
for t in range(1 ,T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    si, sj = lst[0], lst[1]
    ei, ej = lst[2], lst[3]
    locations = []
    visited = [0] * N
    ans = float('inf')
    for i in range(2, N+2//2+1):
        locations.append([lst[2*i], lst[2*i+1]])
    # print(locations)
    dfs(si, sj, 0, 0)
    print(f'#{t} {ans}')

