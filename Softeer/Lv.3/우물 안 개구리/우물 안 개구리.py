import sys
n, m = map(int, sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))
mate = [[] for _ in range(n)]
for _ in range(m):
    i, m = map(int, sys.stdin.readline().split())
    mate[i-1].append(m-1)
    mate[m-1].append(i-1)
ans = 0

for i in range(n):
    max_weight = weights[i]
    flag = True
    for j in mate[i]:
        if max_weight <= weights[j]:
            flag = False
            break
    if flag is True:
        # print(i)
        ans += 1
print(ans)