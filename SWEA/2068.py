T = int(input())
for i in range(T):
    lst = list(map(int, input().split()))
    lst.sort()
    ans = lst[-1]
    print('#'+ str(i+1), end = ' ')
    print(ans)    