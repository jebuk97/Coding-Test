import sys
N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
coins.reverse()
cnt = 0
for c in coins:
    while c <= K:
        K -= c
        # print(K)
        cnt += 1
print(cnt)