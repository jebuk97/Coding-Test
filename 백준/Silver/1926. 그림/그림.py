from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dyx = ((-1, 0), (1, 0), (0, -1), (0, 1))

visited = [[False for _ in range(m)] for _ in range(n)]

def check(c):
    y, x = c
    return 0<=y<n and 0<=x<m

def bfs(stt):
    global visited
    q = deque([stt])
    visited[stt[0]][stt[1]] = True
    cnt = 0
    while len(q):
        cur = q.popleft()
        cnt += 1
        for yx in dyx:
            y, x = yx
            ny, nx = cur[0] + y, cur[1] + x
            if check((ny, nx)) == False:
                continue
            if visited[ny][nx] == False and grid[ny][nx] == 1:
                q.append((ny, nx))
                visited[ny][nx] = True
    return cnt
ans = []
for i in range(n):
    for j in range(m):
        if visited[i][j] == False and grid[i][j] == 1:
            ans.append(bfs((i, j)))

print(len(ans))
if len(ans) > 0:
    print(max(ans))
else:
    print(0)