import sys



def xsolve(matrix, N):
    for l in range(N, 0, -1):
        for txt in matrix:
            for i in range(N-l+1):
                word = txt[i:i + l]
                if word == word[::-1]:

                    return l
        for txt in zip(*matrix):
            for i in range(N-l+1):
                word = txt[i:i + l]
                if word == word[::-1]:
                    return l
sys.stdin =  open('input.txt')

for _ in range(10):
    t = int(input())
    mat  = [input() for _ in range(100)]
    ans = xsolve(mat, len(mat))
    print(f'#{t} {ans}')
