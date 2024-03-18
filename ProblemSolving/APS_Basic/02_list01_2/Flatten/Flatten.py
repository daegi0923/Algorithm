import sys


sys.stdin = open('input.txt')
for t in range(10):
    dump = int(input())
    heights = list(map(int, input().split()))
    for _ in range(dump):
        max_idx = heights.index(max(heights))
        min_idx = heights.index(min(heights))
        if max_idx == min_idx:
            break
        heights[max_idx] = heights[max_idx] - 1
        heights[min_idx] = heights[min_idx] + 1

    print(f'#{t+1} {max(heights) - min(heights)}')