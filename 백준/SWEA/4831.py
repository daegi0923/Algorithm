T = int(input())

for i in range(T):
    K, N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    ans = 0
    idx = 0
    curr = 0
    while True:
        if lst[idx + 1] > lst[idx] + K:
            ans = 0
            break
        
        

        



                   