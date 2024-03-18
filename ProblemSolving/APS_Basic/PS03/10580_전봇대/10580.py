import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ans = 0
    cables = []
    for _ in range(N):
        s, e = map(int, input().split())
        if cables:
            for cable in cables:
                if cable[0] < s and cable[1] > e or cable[0] > s and cable[1]< e:
                    ans = ans + 1
        cables.append([s, e])
    print(f'#{t} {ans}')
