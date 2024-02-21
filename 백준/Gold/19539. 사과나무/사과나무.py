N = int(input())
lst = list(map(int, input().split()))
singles = doubles = 0
flag = 1
for i in range(N):
    if lst[i] % 2:
        singles = singles + 1
    if lst[i] //2 :
        doubles = doubles + lst[i]//2
if doubles < singles:
    flag = 0
if sum(lst)%3:
    flag = 0
# print(doubles, singles)
doubles = doubles - singles
singles = 0
#     print(doubles, singles)
doubles = (doubles * 2)%3
while True:
    if doubles <= 0:
        break
    if singles:
        singles = singles - 1
        doubles = doubles - 1
    elif not singles and doubles:
        doubles = doubles - 2
        singles = singles + 1
# print(singles, doubles)
if not singles and not doubles and flag:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)