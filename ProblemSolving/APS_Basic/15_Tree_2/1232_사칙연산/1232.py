import sys


sys.stdin = open('input.txt')

oper = {
    '+' :(lambda x, y : x + y),
    '-' : (lambda x, y : x - y) ,
    '*': (lambda x, y: x * y),
    '/': (lambda x, y: x / y),
}


def trav(node):
    global tree
    # print(node)
    if str(node['item']).isdigit():
        return node['item']
    else:
        cal = oper[node['item']]
        res = cal(trav(tree[node['left']]), trav(tree[node['right']]))
        return int(res)


T = 10
for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    for _ in range(N):
        lst = list(input().split())
        node = {}
        if len(lst) > 2:
            node['item'] = lst[1]
            node['left'] = int(lst[2])
            node['right'] = int(lst[3])
        else:
            node['item'] = int(lst[1])
        tree[int(lst[0])] = node
    print(f'#{t} {trav(tree[1])}')