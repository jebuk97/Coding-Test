n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for i in range(1, n+1)]
if n == 1:
    print(tri[0][0])
else:
    dp[0][0] = tri[0][0]
    dp[1][0] = tri[1][0] + dp[0][0]
    dp[1][1] = tri[1][1] + dp[0][0]
    if n >= 2:
        for i in range(2, n):
            dp[i][0] = tri[i][0] + dp[i-1][0]
            for j in range(1, len(tri[i])-1):
                dp[i][j] = tri[i][j] + max(dp[i-1][j-1], dp[i-1][j])
            dp[i][len(tri[i])-1] = tri[i][len(tri[i])-1] + dp[i-1][len(tri[i])-2]
    print(max(dp[len(dp)-1]))