def solution(n):
    answer = 0
    for i in range(4, n+1):
        if i % 2 == 0:
            answer += 1
        else:
            for j in range(i-2, 2, -2):
                if i % j == 0:
                    answer += 1
                    break
    return answer