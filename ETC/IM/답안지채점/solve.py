import sys

sys.stdin = open('input.txt')
T = int(input())

def calScore(lst):
    seq = 0
    score = 0
    for idx, ans in enumerate(lst):
        # print(idx, ans, answers[idx], seq, score)
        if ans == answers[idx]:
            score = score + seq
            seq = seq + 1

        else:
            score = score + seq
            seq = 0
    else:
        score = score + seq
    return score



for t in range(1, T+1):
    N, M = map(int, input().split())
    answers = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    scores = [calScore(student) for student in matrix]
    res = max(scores) - min(scores)
    print(f'#{t} {res}')