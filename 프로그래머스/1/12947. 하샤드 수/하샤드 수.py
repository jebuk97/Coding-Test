def solution(x):
    strX = str(x)
    summ = 0
    for s in strX:
        if s == '0':
            continue
        intS = int(s)
        summ += intS
    if x % summ == 0:
        return True 
    else:
        return False
    # return answer