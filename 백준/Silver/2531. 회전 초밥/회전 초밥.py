import sys
n, d, k, c = map(int, sys.stdin.readline().split())
rail = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
lp = 0
rp = 0
ans = 0
while lp != n:
    rp = lp + k
    eat = set()
    for i in range(lp, rp):
        eat.add(rail[i%n])

    eat.add(c)
    ans = max(ans, len(eat))
    lp += 1
    # print(eat)
print(ans)