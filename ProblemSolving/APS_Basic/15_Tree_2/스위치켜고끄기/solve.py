import sys

sys.stdin = open('input.txt')

def toggle(i):
    # print(i)
    lst[i] = (lst[i]+1)%2

n_switches = int(input())
lst = list(map(int, ('0 '+ input()).split()))
n_students = int(input())
for _ in range(n_students):
    gender, num = map(int, input().split()) # 1: male, 2: female
#     print(lst)
    if gender == 1:
        [toggle(idx) for idx in range(n_switches+1) if idx % num == 0]
        [toggle(idx) for idx in range(1, num+1)]
    else:
        sym = []
        for i in range(min(num, n_switches-num+1)):
            # print(lst[num-i], lst[num+i], i)
            if lst[num-i] == lst[num+i]:
                sym.append(num-i)
                sym.append(num+i)
            else:
                break
        # print(sym)
        [toggle(i) for i in range(1, n_switches+1) if i not in sym]

# print(lst)
lst.pop(0)
[print(*lst[i*20:(i+1)*20]) for i in range(n_switches//20+1)]
