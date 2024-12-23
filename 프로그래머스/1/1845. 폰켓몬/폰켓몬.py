def solution(nums):
    hashMap = dict()
    ans = 0
    N = len(nums)
    for num in nums:
        if num in hashMap:
            hashMap[num] = hashMap[num] + 1
        else:
            hashMap[num] = 1
    if len(hashMap) < N/2:
        ans = len(hashMap)
    else:
        ans = N/2
    return ans