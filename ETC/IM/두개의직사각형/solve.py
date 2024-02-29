import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    cnt = [0] * 5
    MAP = [[0] * 1001 for _ in range(1001)]
    ans = 0

    for i in range(1,3):
        x1,y1,x2,y2 = map(int,input().split())
        # print(f'{i}번째 사각형의 좌표',x1,y1,x2,y2)
        for j in range(y1,y2+1): #+1 을해줘야 y2까지 계산가능
            for k in range(x1,x2+1): #+1 을해줘야 y2까지 계산가능
                #사각형의 테두리
                if cnt[4]>2:
                    break
                if j == y1 or j == y2 or k == x1 or k == x2: #j는 언제시작되는가?y1 끝점은?y2
                    MAP[j][k] = MAP[j][k] + 1
                MAP[j][k] = MAP[j][k] + 1
                # print(MAP[j][k])
                cnt[MAP[j][k]] = cnt[MAP[j][k]] + 1

    # print(cnt)
    if cnt[4] == 1:
        ans = 3
    elif cnt[4] > 1 and cnt[3] > 0:
        ans = 1
    elif cnt[4] > 1:
        ans = 2
    else:
        ans = 4
    print(cnt)

    print(f'#{t+1} {ans}')