width, height = map(int, input().split())
t = int(input())
axis_x = []
axis_y = []
for _ in range(t):
    axis, num = map(int, input().split()) # axis-> 0: 가로, 1: 세로
    if axis:
        axis_y.append(num)
    else:
        axis_x.append(num)
axis_x.extend([0, height])
axis_y.extend([0, width])
axis_x.sort()
axis_y.sort()
max_h = 0

max_w = 0
for idx, axis in enumerate(axis_x[:len(axis_x)-1]):
    h = axis_x[idx+1] - axis
    if h > max_h:
        max_h = h
for idx, axis in enumerate(axis_y[:len(axis_y)-1]):
    w = axis_y[idx+1] - axis
    if w > max_w:
        max_w = w
print(max_h*max_w)
