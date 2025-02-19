import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
	n = int(input())
	clothes = dict()
	for i in range(n):
		name, type= input().split()
		# print(type, name)
		if type not in clothes:
			clothes[type] = [name]
		else:
			clothes[type].append(name)
	# print(clothes)
	# print(clothes.keys())
	ans = 1
	for key in clothes.keys():
		# print(clothes[key])
		# print(len(clothes[key]))
		ans = ans * (len(clothes[key])+1)
	print(ans-1)