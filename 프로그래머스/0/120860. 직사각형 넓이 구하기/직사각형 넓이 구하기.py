def solution(dots):
    mini = [1000, 1000]
    maxi = [-1000, -1000]
    for d in dots:
        mini[0] = min(mini[0], d[0])
        mini[1] = min(mini[1], d[1])
        maxi[0] = max(maxi[0], d[0])
        maxi[1] = max(maxi[1], d[1])
    answer = (maxi[0]-mini[0])*(maxi[1]-mini[1])
    return answer