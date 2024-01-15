a = int(input())
ans = 0
lst_max = []
for i in range(a+1):
    lst = []
    lst.append(a)
    lst.append(i)
    num = a - i
    while True:
        if num < 0:
            break
        lst.append(num)
        num = lst[-2] - num
    if len(lst) > ans:
        lst_max = lst
        ans = len(lst)
        
print(ans)
for i in lst_max:
    print(i, end = ' ')