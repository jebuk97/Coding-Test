def solution(dartResult):
    res = list(dartResult)
    save = []
    tmp = ''
    bonus = 1
    for r in res:
        if r == '*':
            save[len(save)-1] *= 2
            if len(save)-2 >= 0:
                save[len(save)-2] *= 2
            continue
        elif r == '#':
            save[len(save)-1] *= -1
            continue
            
        if r == 'S' or r == 'D' or r == 'T':
            if r == 'S':
                bonus = 1
            elif r == 'D':
                bonus = 2
            else:
                bonus = 3
            save.append(int(tmp) ** bonus)
            tmp = ''
            bonus = 1
        else:
            tmp += r
    answer = sum(save)
    return answer