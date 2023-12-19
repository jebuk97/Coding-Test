n = int(input())
nums = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = nums[0]
for i in range(1, len(nums)):
    dp[i] = nums[i]
    for j in range(i-1, -1, -1):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + nums[i])
print(max(dp))