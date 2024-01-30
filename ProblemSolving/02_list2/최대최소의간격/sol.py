import sys


sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    max_idx = 0
    min_idx = nums.index(min(nums))
    max_num = nums[0]
    for idx, num in enumerate(nums):
        if num >= max_num:
            max_num = num
            max_idx = idx
    # print(max_idx, min_idx)
    print(f"#{t+1} {abs(max_idx - min_idx)}")