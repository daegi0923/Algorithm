import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    lstA = list(map(int, input().split()))
    lstB = list(map(int, input().split()))
    lstA.sort()
    ans = 0
    for num in lstB:
        start = 0
        end = N - 1
        d = 0
        while start <= end:
            mid = (start + end) // 2
            if lstA[mid] == num:
                ans = ans + 1
                break
            elif lstA[mid] > num:
                end = mid - 1
                if d == -1:
                    break
                else:
                    d = -1
            else:
                start = mid + 1
                if d == 1:
                    break
                else:
                    d = 1
    print(f'#{t+1} {ans}')