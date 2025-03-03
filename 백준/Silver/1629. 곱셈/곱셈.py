import sys

input = sys.stdin.readline

def power_mod(A, B, C):
    if B == 1:  # B가 1이면 그냥 A % C 반환
        return A % C

    half = power_mod(A, B // 2, C)  # A^(B/2) % C 를 재귀적으로 구함
    half = (half * half) % C  # 제곱해서 다시 % C 적용

    if B % 2 == 1:  # B가 홀수면 A를 한 번 더 곱해줌
        return (half * A) % C
    return half

# 입력 받기
A, B, C = map(int, input().split())
print(power_mod(A, B, C))
