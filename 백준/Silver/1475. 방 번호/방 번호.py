# import sys
#
# sys.stdin = open('input.txt')

N = int(input())
cnt = [0] * 10
for i in str(N):
    cnt[int(i)] += 1
six = (cnt[6] + cnt[9])//2 + (cnt[6] + cnt[9])%2
cnt[6] = six
cnt[9] = six
print(max(cnt))