T = int(input())
for i in range(T):
    ans = 0
    lst = list(map(int, input().split()))
    for j in lst:
        if j % 2 == 1:
            ans += j
    print("#" + str(i + 1), end = ' ')
    print(ans)