def toggle(sw):
    if sw:
        return 0
    else:
        return 1

# 스위치 리스트 입력받고
# 남자일때 여자일때 조건다르게해서 조절


T = int(input()) # # of switches
lst = list(map(int, input().split()))
N = int(input()) # # of students
for _ in range(N):
    gender, num = map(int, input().split())
    if gender == 1:
        for s_num, switch in enumerate(lst):
            if (s_num+1)%num == 0:
                lst[s_num] = toggle(switch)

    elif gender == 2:
        # lst[num-1] = toggle(lst[num-1])
        for sym_len in range(min(num, T - num+1)):
            if lst[num-1 - sym_len] == lst[num -1 + sym_len]:
                lst[num-1 - sym_len] = lst[num-1 + sym_len] = toggle(lst[num-1 - sym_len])
            else:
                break
    # print(lst)
[print(*lst[20 * i: (i+1)*20]) for i in range(T//20+1)]


