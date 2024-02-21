def make_subset(i, target_num, lst , target_sum):
    global set_, cnt
    if len(lst) == target_num:
        if sum(lst) == target_sum:
            cnt = cnt + 1
        return
    if i == len(set_):
        return
    make_subset(i+1, target_num,lst, target_sum)
    if target_sum >= sum(lst, set_[i]):
        lst.append(set_[i])
        make_subset(i+1, target_num,lst, target_sum)
        lst.pop()



T =  int(input())
for t in range(T):
    N, K = map(int, input().split())
    cnt = 0
    set_ = [i for i in range(1, 13)]
    subset = []
    make_subset(0, N, subset, K)
    print(f'#{t+1} {cnt}')