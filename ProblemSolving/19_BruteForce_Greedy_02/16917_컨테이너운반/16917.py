import sys

sys.stdin =  open('input.txt')

# def dfs(i, local_sum):
#     global ans
#     # print(i, local_sum)
#     if i == M:
#         if local_sum > ans:
#             ans = local_sum
#         return
#     for l in range(N):
#         if not used[l]:
#             if weights[l] <= trucks[i]:
#                 used[l] = 1
#                 dfs(i+1, local_sum + weights[l])
#                 used[l] = 0
#             dfs(i+1, local_sum)

T = int(input())
for t in range(1, T+1):
    N ,M = map(int, input().split())
    weights = list(map(int,input().split()))
    trucks = list(map(int,input().split()))
    ans = 0
    used = [0] * (N+1)
    weights.sort(reverse=True)
    trucks.sort(reverse=True)
    truck_num = 0
    luggage_num = 0
    while True:
        if truck_num == M or luggage_num == N:
            break
        if trucks[truck_num] >= weights[luggage_num]:
            ans = ans + weights[luggage_num]
            truck_num = truck_num+1
        luggage_num = luggage_num + 1
    # print(weights)
    # print(trucks)

    print(f'#{t} {ans}')

