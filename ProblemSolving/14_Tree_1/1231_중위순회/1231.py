import sys

sys.stdin = open('input.txt')


def inorder(level, node, tree):
    global ans
    if 'left' in node:
        inorder(level+1, tree[node['left']], tree)
    ans = ans + node['item']
    if 'right' in node:
        inorder(level+1, tree[node['right']], tree)
    return


T =  10
for t in range(1, T+1):
    global lst
    N = int(input())
    tree = [0] * (N+1)
    ans = ""
    for i in range(N):
        temp = list(input().split())
        node = {}
        # node['num'] = int(temp[0])
        node['item'] = temp[1]
        if len(temp) >= 3:
            node['left'] = int(temp[2])
            if len(temp) >= 4:
                node['right'] = int(temp[3])
        tree[int(temp[0])] = node
    # print(tree)
    inorder(0, tree[1], tree)
    print(f'#{t} {ans}')
