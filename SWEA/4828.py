T = int(input())
for i in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = lst[-1]-lst[0]
    print("#"+str(i+1), end = ' ')
    print(ans)