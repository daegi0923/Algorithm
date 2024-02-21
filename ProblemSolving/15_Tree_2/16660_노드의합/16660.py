import sys

sys.stdin = open('input.txt')

def traversal(node_num, height, N):
    # print(node_num)
    if tree[node_num] > 0:
        # print(tree[node_num])
        return tree[node_num]
    else:
        k = node_num%2**height
        left = 2**(height+1)+2*k
        right = 2**(height+1)+2*k + 1
        left_num = right_num = 0
        if left <= N:
            left_num = traversal(left, height + 1, N)
        if right <= N:
            right_num = traversal(right, height+1, N)
        tree[node_num] = left_num + right_num
        return left_num + right_num



T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        node, num = map(int,input().split())
        tree[node] = num
#     print(tree)
    traversal(1, 0, N)
    ans = tree[L]
    print(f'#{t} {ans}')