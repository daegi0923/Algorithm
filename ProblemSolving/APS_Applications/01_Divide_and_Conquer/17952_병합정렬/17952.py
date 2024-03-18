import sys

sys.stdin = open('input.txt')

def mergesort(lst, start, end):
    global ans
    if end - start <= 1:
        return

    mid = (start + end) // 2
    mergesort(lst, start, mid)
    mergesort(lst, mid, end)

    left = lst[start:mid]
    right = lst[mid:end]
    # print(lst, start, mid, end)
    if lst[mid-1] > lst[end-1]:
        ans = ans + 1
    lidx, ridx, idx = 0, 0, start
    while lidx < len(left) and ridx < len(right):
        if left[lidx] > right[ridx]:
            lst[idx] = right[ridx]
            ridx += 1
        else:
            lst[idx] = left[lidx]
            lidx += 1
        idx += 1

    while lidx < len(left):
        lst[idx] = left[lidx]
        lidx += 1
        idx += 1

    while ridx < len(right):
        lst[idx] = right[ridx]
        ridx += 1
        idx += 1


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    mergesort(lst, 0, N)
    print(f'#{t} {lst[N//2]} {ans}')
