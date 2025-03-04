import sys
import heapq

input = sys.stdin.readline

N = int(input())
tree = {}
for _ in range(N):
	parent, left, right = input().split()
	tree[parent] = (left, right)

def postOrder(node):
	if node == '.':
		return
	print(node, end='')
	postOrder(tree[node][0])
	postOrder(tree[node][1])


def preOrder(node):
	if node == '.':
		return

	preOrder(tree[node][0])
	print(node, end='')
	preOrder(tree[node][1])

def inOrder(node):
	if node == '.':
		return

	inOrder(tree[node][0])
	inOrder(tree[node][1])
	print(node, end='')

	pass
# print(tree)

postOrder('A')
print()
preOrder('A')
print()

inOrder('A')
print()
