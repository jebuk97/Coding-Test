N = int(input())
dp = [0] * N
stair = [int(input()) for _ in range(N)]
if N <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = dp[0] + stair[1]
    for i in range(2, N):
        # 가능한 경우: 한칸, 한칸 또는 두칸
        dp[i]=max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
    print(dp[-1])