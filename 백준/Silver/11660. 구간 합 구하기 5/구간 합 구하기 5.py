import sys
N, M = map(int, sys.stdin.readline().split())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = nums[0][0]
for i in range(1, N*N):
    j = i-1
    dp[i//N][i%N] = dp[j//N][j%N] + nums[i//N][i%N]
for _ in range(M):
    a, b, c, d = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    ans = 0
    for i in range(a, c+1):
        # print(dp[i], b)
        if b == 0:
            if i == 0:
                ans += dp[i][d]
            else:
                # print(dp[i][d], dp[i-1][d])
                ans += dp[i][d] - dp[i-1][N-1]
        else:
            ans += dp[i][d] - dp[i][b-1]
    print(ans)