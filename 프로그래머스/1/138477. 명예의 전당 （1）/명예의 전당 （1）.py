def solution(k, score):
    scores = []
    answer = []
    for s in score:
        if len(scores) < k:
            scores.append(s)
        else:
            min_s =  min(scores)
            if min_s < s:
                scores[scores.index(min_s)] = s
        answer.append(min(scores))
    return answer