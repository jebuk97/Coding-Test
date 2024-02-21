import math
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        tmp = math.sqrt(i)
        if (tmp - tmp//1) == 0:
            answer -= i
        else:
            answer += i
    return answer