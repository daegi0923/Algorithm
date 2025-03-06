import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))

def cut_tree(trees, height):
	return sum(tree - height for tree in trees if tree > height)


def find_max_height(n, m, trees):
	left, right = 0, max(trees)

	while left <= right:
		mid = (left + right) // 2
		wood = cut_tree(trees, mid)

		if wood >= m:  # 충분한 나무를 얻을 수 있으면 더 높은 절단 높이 탐색
			result = mid
			left = mid + 1
		else:  # 얻은 나무가 부족하면 절단 높이를 낮춤
			right = mid - 1

	return result

print(find_max_height(N, M, trees))