# sort, sum,min 내장함수 사용하지 않고 풀어보기
# selection sort 연습

import sys

def specialSort(lst, n):
    for i in range(n):
        target = i
        if i % 2 == 0:
            for j in range(n-i):
                if lst[i+j] > lst[target]:
                    target = i + j
        else:
            for j in range(n - i):
                if lst[i + j] < lst[target]:
                    target = i + j
        lst[i], lst[target] = lst[target], lst[i]



sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int,input().split()))
    specialSort(lst, N)
    print(f'#{t+1}', *lst[:10])