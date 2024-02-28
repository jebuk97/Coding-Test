def solution(k, m, score):
    boxes = len(score) // m
    score.sort(reverse = True)
    answer = 0
    for i in range(boxes):
        answer += score[(i+1)*m-1]*m
    print(answer)
    return answer