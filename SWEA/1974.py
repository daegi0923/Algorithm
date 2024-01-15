T = int(input())
for t in range(T):
    mat = []
    for i in range(9):
        lst = list(map(int, input().split()))
        mat.append(lst)
    rowsum = [0] * 9
    colsum = [0] * 9
    squareSum = [0] * 9
    for i in range(9):
        rowsum[i] += sum(mat[i])
        
    for i in range(9):
        for j in range(9):
            colsum[i] += mat[i][j] 
    
    
    for i in range(3):
        for j in range(3):
            num = 0
            for k in range(3):
                for l in range(3):
                    num += mat[3*i + k][3*j + l]
            squareSum[i + 3*j] = num
    ans = 1
    for i in squareSum:
        if i != 45:
            ans = 0
    for i in colsum:
        if i != 45:
            ans = 0
    for i in rowsum:
        if i != 45:
            ans = 0
    
    print('#{} {}'.format(T, ans))