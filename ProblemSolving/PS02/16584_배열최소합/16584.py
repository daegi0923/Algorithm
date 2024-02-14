import sys

sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    for idx, row in enumerate(mat):


