import math
def solution(brown, yellow):
    '''
    n, m
    3+3+2, 3-2 [3, 3]
    3+3+2+2, 3+3-2-2 [3, 4]
    n+n+2(m-n+1), (m-2)*(n-2)
    ?+?+2+2, ?-2 [?, 4]
    6, 0 = [3, 2]
    8, 1 = [3, 3]
    9, 1 = [3, 4]
    12, 4 = [4, 4]
    10, 2 = [4, 3]
    16, 9 = [5, 5]
    x+1 = +2, +1
    y+1 = 0, +1
    n, 2, 2, n
    '''
    # print(brown+yellow)
    # print(math.sqrt(brown+yellow))
    for i in range(3, brown):
        if (brown+yellow)%i == 0:
            tmp = [(brown+yellow)/i, i]
            n = tmp[0]
            m = tmp[1]
            if n >= m:
                if (brown == (2*n+2*(m-2))) and (yellow == ((m-2)*(n-2))):
                    return ([int(tmp[0]), int(tmp[1])])
                    # print(2*n+2*(m-2))
                    # print((m-2)*(n-2))
    answer = []
    return answer