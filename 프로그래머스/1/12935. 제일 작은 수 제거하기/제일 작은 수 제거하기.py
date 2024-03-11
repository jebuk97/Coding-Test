def solution(arr):
    
    answer = []
    mini = min(arr)
    for a in arr:
        if a == mini:
            continue
        answer.append(a)
    if len(answer) == 0:
        return answer[-1]
    return answer