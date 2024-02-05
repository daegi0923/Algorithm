n = int(input())
ans = 0
while True:
    if n%5 == 0:
        ans = ans + n//5
        break
    else:
        n = n-2
        ans = ans + 1
    if n < 0:
        ans = -1
        break
print(ans)
