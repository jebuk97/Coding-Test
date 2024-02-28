from collections import defaultdict
def solution(s):
    answer = []
    save = defaultdict(int)
    for i in range(len(s)):
        if save[s[i]] == 0:
            answer.append(-1)
        else:
            answer.append(i-save[s[i]]+1)
        save[s[i]] = i + 1
    return answer