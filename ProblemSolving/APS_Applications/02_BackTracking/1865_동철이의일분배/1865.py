import sys
sys.stdin = open('input.txt')

def cal_p(k, prob):
    global ans, cnt
    cnt = cnt + 1
    if k == N:
        if ans < prob:
            ans = prob
        return
    for work_num in range(N):
        if not assigned[work_num] and prob*p_mat[k][work_num]*0.01 > ans:
            assigned[work_num] = 1
            cal_p(k+1, prob * p_mat[k][work_num]*0.01)
            assigned[work_num] = 0




T = int(input())
for t in range(1, T+1):
    N = int(input())
    # print(N)
    p_mat = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    assigned = [0]*(N+1)
    cnt = 0
    cal_p(0, 1)
    print(f'#{t} {ans*100:.6f}')
