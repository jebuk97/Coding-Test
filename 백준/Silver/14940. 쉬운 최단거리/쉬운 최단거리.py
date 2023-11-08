from collections import deque
n, m = map(int, input().split())
grid = []
stt = None
for i in range(n):
    col = list(map(int, input().split()))
    if stt is None and 2 in col:
        stt = (i, col.index(2))
    grid.append(col)

dyx = ((-1, 0), (1, 0), (0, -1), (0, 1))

def check(c):
    return 0<=c[0]<n and 0<=c[1]<m

def bfs():
    visited = [[-1] * m for _ in range(n)]
    q = deque([(stt, 0)])
    visited[stt[0]][stt[1]] = 0
    while len(q) > 0:
        cur, dist = q.popleft()
        for yx in dyx:
            ny, nx = cur[0] + yx[0], cur[1] + yx[1]
            if (ny, nx) != stt and check((ny, nx)) == True and visited[ny][nx] == -1:
                if grid[ny][nx] == 0:
                    visited[ny][nx] = 0
                    continue
                q.append(((ny, nx), dist+1))
                visited[ny][nx] = dist+1

    visited[stt[0]][stt[1]] = 0
    return visited

ans = bfs()
for i, a in enumerate(ans):
    for j, aa in enumerate(a):
        if grid[i][j] == 0:
            ans[i][j] = 0
for a in ans:
    print(*a)