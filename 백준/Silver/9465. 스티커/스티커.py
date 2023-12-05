T = int(input())
for _ in range(T):
    n = int(input())
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))
    dp = [[0]*2 for _ in range(n)]
    dp[0][0] = row1[0]
    dp[0][1] = row2[0]
    if n > 1:
        dp[1][0] = dp[0][1] + row1[1]
        dp[1][1] = dp[0][0] + row2[1]
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][1], dp[i-2][1]) + row1[i]
            dp[i][1] = max(dp[i-1][0], dp[i-2][0]) + row2[i]

    print(max(dp[n-1]))