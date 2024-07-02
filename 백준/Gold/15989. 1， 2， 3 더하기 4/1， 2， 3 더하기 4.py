lst = [0] * 10001
T = int(input())
last = 3
lst[1] = 1
lst[2] = 2
lst[3] = 3
for _ in range(T):
    n = int(input())
    if n > last:
        for i in range(last+1, n+1):
            lst[i] = lst[i-3] + i//2 +1
    print(lst[n])
    # print(lst)


