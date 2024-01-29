num = int(input())
ans = 0
while True:
    if num == 0:
        break
    ans += num%10
    num = num // 10
print( ans )