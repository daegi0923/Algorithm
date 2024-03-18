'''
몇명의 학생은 1 이상 스위치 개수 이하 자연수 배정 받음

남학생: 스위치 번호가 자기가 받은 수의 배수이면, 스위치 상태 변경(3번 배정 -> 3, 6 스위치 변경)
++ 변경사항: 위 조건문 수행 후 '1번부터 자기가 받은 수의 스위치 번호까지' 상태 변경 추가(3번 배정 -> 1, 2, 3번 스위치 상태 변경)
++ (사실상 3번의 경우 스위치 변경 안된거나 마찬가지)
여학생: 받은 번호 스위치 기준 대칭이면서 가장 많은 스위치 포함한 구간의 모든 스위치 변경(항상 스위치 개수 홀수, 대칭되는 구간 없다면, 본인 번호 스위치만 변경)
++ 변경사항: 위 조건과 반대로, 대칭인 구간을 '제외'하고, 나머지 모든 스위치 상태 변경으로 수정

원본 출처: https://www.acmicpc.net/problem/1244
'''

import sys

sys.stdin = open('input.txt')

switch_cnt = int(input())       # 스위치 개수
current_status = list(map(int, input().split()))    # 현재 스위치 상태
student_cnt = int(input())      # 학생 수

current_status.insert(0, 0)     # index 그대로 switch 번호로 사용하기 위해 맨 앞에 0 추가
# print(current_status)
for _ in range(student_cnt):
    gender, number = map(int, input().split())      # gender: 1 남자, 2 여자
    if gender == 1:     # 남자라면,
        for i in range(1, switch_cnt + 1):
            if i >= number and i % number == 0:     # 모든 스위치 중 받은 번호 배수의 스위치만 변경하기 위한 조건문
                current_status[i] = (current_status[i] + 1) % 2     # 0이라면 1로, 1이라면 0으로 바꾸는 수식

        for i in range(1, number + 1):              # 1번부터 받은 스위치 번호까지 상태 변경
            current_status[i] = (current_status[i] + 1) % 2

    elif gender == 2:   # 여자라면,
        max_cnt = min(number - 1, switch_cnt - number)    # 오른쪽 최대 개수, 왼쪽 최대 개수 중 작은 값
        for i in range(max_cnt + 1):        # max_cnt만큼 양쪽으로 슬라이싱하기 위해, 반복하면서 대칭인지 확인
            if current_status[number - i:number + i + 1] == current_status[number - i:number + i + 1][::-1]:
                start_idx, end_idx = number - i, number + i     # 최대 대칭인 start_idx, end_idx 저장

        for idx in range(1, start_idx):                   # 1번부터 start_idx - 1번 스위치까지 상태 변경
            # print(idx)
            current_status[idx] = (current_status[idx] + 1) % 2

        for idx in range(end_idx + 1, switch_cnt + 1):    # end_idx + 1번 스위치부터 마지막 스위치까지 상태 변경
#             print(idx)
            current_status[idx] = (current_status[idx] + 1) % 2
#     print(current_status)

for i in range(1, switch_cnt + 1):
    if i >= 20 and i % 20 == 0:             # 20개씩 끊어서 출력해야하기 때문에 조건문 추가
        print(current_status[i])
    else:
        print(current_status[i], end=' ')

print('윤대영')