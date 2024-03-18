import sys

def selectionSort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(0, len(lst)-i):
            if lst[i+j] < lst[min_idx]:
                min_idx = i+j
                # print(min_idx, lst[min_idx])
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int,input().split()))
    selectionSort(lst)
    print(f'#{t+1}',*lst)