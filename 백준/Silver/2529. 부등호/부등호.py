ans = []
def checkString(num1, num2, bracket):
    if bracket == '>':
        return int(num1) > int(num2)
    if bracket == '<':
        return int(num1) < int(num2)


def check_num(cnt, number):
    global brackets
    global isUsed
    global ans
    for i in range(10):
        if k+1 == len(number):
            # print(number)
            ans.append(number)
            return
        if isUsed[i] == True:
            continue


        if cnt == 0 or checkString(number[cnt-1], str(i), brackets[cnt-1]):
            isUsed[i] = True
            check_num(cnt + 1, number + str(i))
            isUsed[i] = False

k = int(input())
brackets = list(input().split())
nums = list(range(10))
exp = ""
curr = 0
isUsed = [False] * 10
check_num(0, "")
print(ans[-1])
print(ans[0])


