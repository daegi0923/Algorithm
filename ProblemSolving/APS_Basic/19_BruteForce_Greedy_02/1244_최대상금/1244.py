import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    nums , N = map(int, input().split())
    nums = list(str(nums))
    n_nums = len(nums)
    # print(nums, N)
    ans = 0
    cnt = 0
    target = 0
    order = 0
    while True:
        while True:
            # print(target, n_nums-2)
            if target < n_nums and nums[target] == max(nums[target:]) :
                target =  target +1
            else:
                break
        # print(cnt, target)
        if cnt == N or target == n_nums:
            break
        if target < n_nums:
            swap_target = nums[n_nums-1]
            swap_idx = n_nums-1
            for idx in range(n_nums-1, -1+target, -1):
                if nums[idx] > swap_target:
                    swap_target = nums[idx]
                    swap_idx = idx
                    order = 1
                elif nums[idx] == swap_target and order < (N-cnt):
                    order = order + 1
                    swap_idx = idx
                    swap_target = nums[idx]

            nums[target], nums[swap_idx] = nums[swap_idx], nums[target]
            cnt = cnt + 1
            target = target + 1
    max_count = max(nums.count(i) for i in nums)
    if (N-cnt)%2 and max_count == 1:
        nums[-1], nums[-2] = nums[-2], nums[-1]
    ans = int(''.join(nums))
    print(f'#{t} {ans}')