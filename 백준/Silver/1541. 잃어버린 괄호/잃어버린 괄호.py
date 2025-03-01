import sys

input = sys.stdin.readline

syntax = input().strip()

# '-' 기준으로 분리
parts = syntax.split('-')

# 첫 번째 그룹은 무조건 더함
ans = sum(map(int, parts[0].split('+')))

# 이후 그룹들은 모두 더한 후 한 번에 뺌
for part in parts[1:]:
    ans -= sum(map(int, part.split('+')))

print(ans)
