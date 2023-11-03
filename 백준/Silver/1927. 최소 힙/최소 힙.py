import heapq
import sys
N = int(sys.stdin.readline())
q = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, n)
    # print(q)