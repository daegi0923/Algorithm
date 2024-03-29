import sys

sys.stdin =  open('input.txt')


def get_idx(target):
    s, e = 0, n-1
    while True:
        mid = (s+e) // 2

        # print(s, e, mid)
        if lst[mid] == target:
            return mid
            break
        if mid == 0 or mid == n-1:
            return 0
        if s == e:
            return 0
        if lst[mid] < target:
            s = mid + 1
        else:
            e = mid


n, q = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
dict = {}
print(lst)
for i, num in enumerate(lst):
    dict[num] = i
for _ in range(q):
    m = int(input())
    idx = get_idx(m)
    print(idx * (n-idx-1))
