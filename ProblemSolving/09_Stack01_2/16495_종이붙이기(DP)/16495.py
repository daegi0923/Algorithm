T = int(input())
cnts = [0] * 31
cnts[0] = 1
cnts[1] = 1
for t in range(T):
    N = int(input())//10
    for idx, cnt in enumerate(cnts[:N+1]):
        if cnt == 0 and idx > 1:
            cnts[idx] = cnts[idx-1] + 2 * cnts[idx-2]
    print(cnts)
    print(f'#{t+1} {cnts[N]}')