import sys


sys.stdin = open('input.txt')

def addTree(node_num, item):
    height = 0
    while True:
        if 2**(height+1) > node_num:
            break
        height = height + 1
    tree[node_num] = item
    height_node[node_num] = height
    checkParent(node_num, height)

def checkParent(node_num, height):
    if height ==0:
        return
    k = node_num % 2 ** height
    parent = 2**(height -1) + k//2
    if tree[parent] > tree[node_num]:
        temp = tree[parent]
        tree[parent] = tree[node_num]
        tree[node_num] = temp
        checkParent(parent, height-1)

def addAncestor(node_num, sum_):
    global ans
    if node_num == 1:
        ans = sum_
        return
    k = node_num % 2 ** height_node[node_num]
    parent = 2**(height_node[node_num]-1) + k//2
    addAncestor(parent, sum_+tree[parent])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    height_node = [0] * (N+1)

    lst = list(map(int, input().split()))
    for idx in range(1, N+1):
        addTree(idx, lst[idx-1])
    addAncestor(N, 0)
    print(f'#{t} {ans}')
