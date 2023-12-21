n = int(input())
boxes = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
    dp[i] = 1
    for j in range(i, -1, -1):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
