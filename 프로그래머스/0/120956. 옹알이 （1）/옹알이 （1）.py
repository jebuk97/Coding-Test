from itertools import permutations
def solution(babbling):
    pron = ['aya', 'ye', 'woo', 'ma']
    all = []
    answer = 0
    for i in range(1, len(pron)+1):
        for b in permutations(pron, i):
            summ = ''
            for j in range(i):
                summ += b[j]
                all.append(summ)
    for b in babbling:
        if b in all:
            answer += 1
    return answer