def solution(n, m):
    answer = [0, 0]
    a = m
    b = n
    while b != 0:
        tmp = a%b
        a = b
        b = tmp
    answer[0] = a

    answer[1] = (m*n)/answer[0]
        
    print(answer)
    return answer