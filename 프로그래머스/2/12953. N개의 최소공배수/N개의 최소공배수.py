from itertools import combinations
def solution(arr):
    m = max(arr)
    i = 1
    while True:
        tmp = m * i
        flag = True
        for j in range(len(arr)):
            if tmp % arr[j] != 0:
                flag = False
        i += 1     
        if flag is True:
            return tmp
            break
    
        