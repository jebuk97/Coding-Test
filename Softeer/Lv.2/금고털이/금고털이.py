import sys
W, N = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
jewels.sort(key = lambda x:-x[1])
ans = 0
for j in jewels:
    if W >= j[0]:
        ans += j[0] * j[1]
        W -= j[0]
    else:
        ans += W * j[1]
        break
print(ans)