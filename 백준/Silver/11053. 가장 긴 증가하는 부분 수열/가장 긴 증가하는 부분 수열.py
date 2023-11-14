n = int(input())
nums = list(map(int, input().split()))
dp = [1] * 1001
for i in range(1, len(nums)):
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))