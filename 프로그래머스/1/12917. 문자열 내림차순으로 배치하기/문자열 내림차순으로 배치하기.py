def solution(s):
    answer = ''.join(sorted(list(s), reverse = True))
    print(answer)
    return answer