def solution(sizes):
    newSizes = []
    for s in sizes:
        newSizes.append(sorted(s, key = lambda x: -x))
    w = sorted(newSizes, key = lambda x: -x[0])
    h = sorted(newSizes, key = lambda x: -x[1])
    answer = w[0][0] * h[0][1]
    return answer