n = int(input())
loc = 0
num = 0
for i in range(1, 10000000):
    num += i
    loc += 1
    if num >= n:
        break
head = n-(num-loc)
tail = loc+1 - head
if loc%2 == 0:
    print("%d/%d" %(head, tail))
else :
    print("%d/%d" %(tail, head))