import sys


sys.stdin = open('input.txt')
nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
dic = {}
for num in nums:
    dic[num] = nums.index(num)
    # dic에 num과 index 넣기
    # ex) dic["ZRO"] = 0
T = int(input())
for _ in range(T):
    t, N = input().split()
    input_lst = list(input().split())
    input_lst.sort(key=lambda x : dic[x]) # 딕셔너리의 키 값의 밸류를 기준으로 정렬
    print(t)
    print(*input_lst)