from itertools import permutations, combinations
def solution(clothes):
    dict = {}
    for c in clothes:
        try:
            dict[c[1]].add(c[0])
        except:   
            dict[c[1]] = set([c[0]])
    
    answer = 1
    for i in dict.values():
        answer *= len(i)+1
                
    return answer-1