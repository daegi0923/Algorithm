import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

cnt = [0] * 10
l = 0
r = 0
ans = 0
while r < N:
	cnt[lst[r]] += 1  # 현재 r번째 과일 추가
	r += 1  # r을 한 칸 이동

	check = sum(1 for i in range(1, 10) if cnt[i] > 0)
	# 만약 3개 이상의 과일이 포함되면 l을 이동시키면서 줄이기
	while check > 2:
		cnt[lst[l]] -= 1
		if cnt[lst[l]] == 0:
			check -= 1  # 종류 하나 줄어들었을 경우 반영
		l += 1

	# 최대 길이 갱신
	ans = max(ans, r - l)

print(ans)