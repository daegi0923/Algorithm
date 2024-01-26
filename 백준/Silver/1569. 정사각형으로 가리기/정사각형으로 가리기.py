def is_available(points,x_points, y_points):
    flag = 0
    check_list = []
    min_x, max_x, min_y, max_y = min(x_points), max(x_points), min(y_points), max(y_points)
    if (max(x_points) - min(x_points)) < (max(y_points)- min(y_points)):
        length = (max(y_points)- min(y_points))
        check = 0
    else:
        length = (max(x_points) - min(x_points))
        check = 1
    
    for point in points:
        x, y = point
        if check == 1 and x not in (max(x_points), min(x_points)):
            check_list.append(y)
        if check == 0 and y not in (max(y_points), min(y_points)):
            check_list.append(x)

    if len(check_list) == 0:
        return True
    if check == 1:
        for c in check_list:
            if c not in (min_y ,min_y + length):
                flag = 1
        if flag == 1:
            for c in check_list:
                if c not in (max_y, max_y-length):
                    flag = 2
    else:
        for c in check_list:
            if c not in (min_x ,min_x + length):
                flag = 1
        if flag == 1:
            for c in check_list:
                if c not in (max_x, max_x-length):
                    flag = 2
    if flag == 2:
        return False
    else:
        return True







N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
# print(points)
x_points = []
y_points = []
flag = 0
for idx, point in enumerate(points):
    x, y = point
    x_points.append(x)
    y_points.append(y)
    

x_length = max(x_points) - min(x_points)
y_length = max(y_points) - min(y_points)
# print(max(x_points), min(x_points))
# print(max(y_points), min(y_points))
# print(x_length, y_length)
# print(is_available(points, (max(x_points), min(x_points)), (max(y_points), min(y_points))))
if (x_length == 0 or y_length == 0) or is_available(points, (max(x_points), min(x_points)), (max(y_points), min(y_points))):
    print(max(x_length, y_length))

else:
    print(-1)