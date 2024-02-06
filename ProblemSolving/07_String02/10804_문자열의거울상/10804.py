import sys

sys.stdin = open('input.txt')

mirror = {'b':'d',
          'd':'b',
          'p':'q',
          'q':'p'}
T = int(input())
for t in range(T):
    string = input()
    ans = ''
    for c in string[::-1]:
        ans = ans + mirror[c]
    print(f'#{t+1} {ans}')