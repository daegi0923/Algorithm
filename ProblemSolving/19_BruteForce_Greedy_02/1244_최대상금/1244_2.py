import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    numbers, count = input().split()
    # print(numbers,count)
    count = int(count)
    nums = set([numbers])
    print(nums)

    SET = set()

    for _ in range(count):
        while nums:
            n = nums.pop()
            n = list(n)
            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    # print(i,j)
                    n[i], n[j] = n[j], n[i]
                    SET.add(''.join(n))
                    n[i], n[j] = n[j], n[i]
        nums, SET = SET, nums



    # print(nums)
    result = max(nums)


    print(f'#{t+1} {result}')