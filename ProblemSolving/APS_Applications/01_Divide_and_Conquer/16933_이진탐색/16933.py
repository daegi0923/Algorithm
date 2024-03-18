import sys
sys.stdin = open('input.txt')

def binary_search(start, end, target):
    global ans, d
    mid = (start + end)//2
    if A[mid] == target:
        # print(mid, target)
        ans = ans + 1
        return
    elif A[mid] < target:
        if d == 1:
            return
        else:
            d = 1
            binary_search(mid+1, end, target)
    elif A[mid] > target:
        if d == 0:
            return
        else:
            d = 0
            binary_search(start, mid-1, target)



T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    ans = 0
    for b in B:
        d = -1
        if b in A:

            binary_search(0, N-1, b)
    print(f'#{t} {ans}')