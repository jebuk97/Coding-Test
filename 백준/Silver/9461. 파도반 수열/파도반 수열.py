T = int(input())
for _ in range(T):
    n = int(input())
    dp = [1 for _ in range(n+1)]
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2]
    print(dp[n])