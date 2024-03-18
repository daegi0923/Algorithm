import sys
sys.stdin = open('input.txt')

def check_quarter(k, s):
    global ans
    if k >= 11:
        if k == 11 :
            if s+counts[k] < ans:
                ans = s+counts[k]
        else:
            if s < ans:
                ans = s
        return
    if k < 10 and fees[2] < counts[k] + counts[k+1] + counts[k+2]:
        # print(k, s, fees[2])
        check_quarter(k+3, s+fees[2])

    check_quarter(k+1, s+counts[k])

T = int(input())
for t in range(1, T+1):
    fees = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    for idx, c in enumerate(counts):
        counts[idx] = c*fees[0]
    for idx, c in enumerate(counts):
        if fees[1] < c:
            counts[idx] = fees[1]
    ans = sum(counts)
    # print(counts)
    check_quarter(0, 0)
    if ans > fees[3]:
        ans = fees[3]
    print(f'#{t} {ans}')