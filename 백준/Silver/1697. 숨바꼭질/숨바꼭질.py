from collections import deque
N, K = map(int, input().split())

def bfs():
    q = deque()
    visited = [False] * 100001
    q.append((N, 0))
    visited[N] = True
    if N == K:
        return 0
    while len(q) > 0:
        cur, sec = q.popleft()
        if cur == K:
            return sec
        dx = (cur + 1, cur - 1, cur * 2)
        for nx in dx:
            if (0 <= nx <= 100000) and visited[nx] is False:
                q.append((nx, sec + 1))
                visited[nx] = True
        # print(visited[N:K])
print(bfs())