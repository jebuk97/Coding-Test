'''
1-1. 숫자가 짝수이면 2로 나눈다.
1-2. 숫자가 홀수이면 3을 곱하고 1을 더한다.
2. 숫자가 1이 되는 경우 현재 횟수를 return

1이 입력되면 0 return
500번 진행하여 1이 되지 않으면 -1 return
'''
def solution(num):
    if num == 1:
        return 0
    for i in range(0, 500):
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        if num == 1:
            return i+1
    return -1