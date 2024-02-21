import sys

sys.stdin = open('input.txt')

def inorder(node, level, max_level, max_num):
    global num
    n = node - 2**(level)
    left = 2**(level+1) + 2*n
    right = 2**(level+1) + 2* n + 1
    if level > max_level or num > max_num:
        return
    if left <= max_num:
        inorder(left, level+ 1, max_level, max_num)
    binary_tree[node] = num
    num = num + 1
    if right <= max_num:
        inorder(right, level+1, max_level, max_num)
    return



T = int(input())

for t in range(1, T+1):
    N = int(input())
    height = 0
    for i in range(N):
        if 2**(i+1)-1 >= N:
            height = i
            break

    max_node = (2**(height+1)-1)
    binary_tree = [0] * (max_node+1)
    num = 1
    inorder(1, 0, height, N)
    print(f'#{t} {binary_tree[1]} {binary_tree[N//2]}')