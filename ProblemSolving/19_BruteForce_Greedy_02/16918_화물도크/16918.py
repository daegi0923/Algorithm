import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    time_table = []
    check_table = [0] * 25
    for _ in range(N):
        s, e = map(int,input().split())
        time_table.append([s, e])
    time_table.sort(key=lambda x:x[1])
    # print(time_table)
    for t in time_table:
        s, e = t
        if sum(check_table[s:e]) == 0:
            ans = ans + 1
            for i in range(s, e):
                check_table[i] = 1


    print(f'#{tc} {ans}')