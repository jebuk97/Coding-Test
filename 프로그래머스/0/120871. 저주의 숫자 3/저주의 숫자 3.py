def solution(n):
    answer = 0
    cnt = 0
    while cnt != n:
        answer += 1
        cnt += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
        print(answer)
            
    return answer