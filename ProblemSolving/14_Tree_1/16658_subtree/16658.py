import sys

sys.stdin = open('input.txt')
def traversal(node):
    global ans
    ans = ans + 1
    if tree[node]:
        childs = tree[node]
        for child in childs:
            traversal(child)

T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    tree = [[] for _ in range(E+2)]
    temp = list(map(int, input().split()))
    for i in range(E):
        parent, child = temp[2*i], temp[2*i+1]
        tree[parent].append(child)
    ans = 0
    traversal(N)
    print(f'#{t} {ans}')
