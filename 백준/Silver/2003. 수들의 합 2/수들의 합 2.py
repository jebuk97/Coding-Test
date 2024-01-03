import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
lp = 0
rp = 1
while lp <= rp and rp <= n:
    tmp = sum(a[lp:rp])
    if tmp <= m:
        rp += 1
        if tmp == m:
            cnt += 1
    elif tmp > m:
        lp += 1
print(cnt)
