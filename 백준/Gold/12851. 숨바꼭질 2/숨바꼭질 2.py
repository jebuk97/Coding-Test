from collections import deque
N, K = map(int, input().split())

def bfs():
    q = deque([(N, 0)])
    visited = [0 for _ in range(100002)]
    visited[N] = True
    short = 999999
    routes = 0
    while len(q) > 0:
        cur, cnt = q.popleft()
        if cnt > short:
            continue
        if cur == K:
            if short == 999999:
                short = cnt
            if short == cnt:
                routes += 1
        nxt = (cur-1, cur+1, cur*2)
        for n in nxt:
            if 0 <= n <= 100001 and (visited[n] == 0 or visited[n]==cnt+1):
                q.append((n, cnt+1))
                visited[n] = cnt + 1

    return short, routes

ans = bfs()
print(ans[0])
print(ans[1])