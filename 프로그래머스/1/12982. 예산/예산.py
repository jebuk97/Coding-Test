def solution(d, budget):
    d.sort()
    i = 0
    while budget > 0 and i < len(d):
        if budget - d[i] < 0:
            break
        else:
            budget -= d[i]
            i += 1
    answer = i
    return answer