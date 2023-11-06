
n = int(input())
if n < 9:
    dp = [0, 0, 0, 1, -1, 1, 2, -1, 2]
    print(dp[n])
else:
    dp = [-1] * (n+1)
    dp[3] = 1
    dp[4] = -1
    dp[5] = 1
    dp[6] = 2
    dp[7] = -1
    dp[8] = 2
    for i in range(9, n+1):
        if dp[i-3] == -1 and dp[i-5] == -1:
            dp[i] = -1
            continue
        if dp[i-3] == -1 and dp[i-5] != -1:
            dp[i] = dp[i-5] + 1
            continue
        if dp[i-3] != -1 and dp[i-5] == -1:
            dp[i] = dp[i-3] + 1
            continue
        dp[i] = min(dp[i-3], dp[i-5]) + 1
    print(dp[n])