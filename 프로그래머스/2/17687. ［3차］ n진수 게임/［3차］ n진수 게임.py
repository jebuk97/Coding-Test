def solution(n, t, m, p):
    tmp = ''
    dp = {}
    for i in range(0, n):
        if i == 10:
            dp[i] = 'A'
        elif i == 11:
            dp[i] = 'B'
        elif i == 12:
            dp[i] = 'C'
        elif i == 13:
            dp[i] = 'D'
        elif i == 14:
            dp[i] = 'E'
        elif i == 15:
            dp[i] = 'F'
        else:
            dp[i] = str(i)
        tmp += str(dp[i])
    dp[n] = '10'
    tmp += '10'
    # print(dp)
    
    i = n+1
    while True:
        if i%n == 10:
            dp[i] = dp[i//n]+'A'
        elif i%n == 11:
            dp[i] = dp[i//n]+'B'
        elif i%n == 12:
            dp[i] = dp[i//n]+'C'
        elif i%n == 13:
            dp[i] = dp[i//n]+'D'
        elif i%n == 14:
            dp[i] = dp[i//n]+'E'
        elif i%n == 15:
            dp[i] = dp[i//n]+'F'
        else:
            dp[i] = dp[i//n]+str(i%n)
        
        tmp += str(dp[i])
        # print(dp, tmp)
        if len(tmp) > t*m:
            break
        i += 1
    answer = ''
    tmp = list(tmp)
    # print(tmp)
    for i in range(len(tmp)):
        if i % m == p-1:
            answer+=tmp[i]
        if len(answer) == t:
            break
    # print(answer)
    return answer