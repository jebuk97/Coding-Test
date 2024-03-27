from itertools import permutations
import copy
def solution(expression):
    exp = []
    num = []
    tmp = ''
    for e in expression:
        if e.isdigit():
            tmp += e
        else:
            num.append(int(tmp))
            tmp = ''
            exp.append(e)
    num.append(int(tmp))
    res = []
    for e in permutations(('*', '-', '+'), 3):
        tmpNum = copy.deepcopy(num)
        tmpExp = copy.deepcopy(exp)
        for ex in e:
            while True:
                try:
                    idx = tmpExp.index(ex)
                    tmpExp.pop(idx)
                    one = tmpNum.pop(idx)
                    if ex == '*':
                        tmpNum[idx] = one * tmpNum[idx]
                    elif ex == '-':
                        tmpNum[idx] = one - tmpNum[idx]
                    elif ex == '+':
                        tmpNum[idx] = one + tmpNum[idx]
                except:
                    break
        
        res.append(abs(tmpNum[0]))
    
    answer = max(res)
    return answer