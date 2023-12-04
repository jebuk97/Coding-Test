from collections import deque
n, k = map(int, input().split())
visited = [False for _ in range(100001)]
visited2 = [False for _ in range(100001)]
# print(visited)
def bfs():
    q = deque([(n, 0)])
    visited[n] = True
    visited2[n] = True

    while len(q) > 0:
        # print(q)
        cur, cnt = q.popleft()
        if cur == k:
            return cnt
        for i in (cur*2, cur-1, cur+1):
            if i < 0 or i > 100000:
                continue
            if i == cur*2:
                if visited2[i] == False:
                    q.append((i, cnt))
                    visited2[i] = True
            elif i == cur + 1 or i == cur-1:
                if visited[i] == False:
                    q.append((i, cnt+1))
                    visited[i] = True

print(bfs())