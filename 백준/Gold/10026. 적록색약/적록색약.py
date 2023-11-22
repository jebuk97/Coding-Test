from collections import deque
N = int(input())
grid = [list(input()) for _ in range(N)]

def check(c):
    return 0<=c[0]<N and 0<=c[1]<N

dyx = ((0, 1), (1, 0), (0, -1), (-1, 0))

visited = [[False for _ in range(N)] for _ in range(N)]
def bfs(stt):
    global visited, grid
    cnt = 0
    q = deque([stt])
    color = grid[stt[0]][stt[1]]
    visited[stt[0]][stt[1]] = True
    while len(q)>0:
        cur = q.popleft()
        cnt += 1
        for y, x in dyx:
            ny, nx = cur[0]+y, cur[1]+x
            if check((ny, nx)) == True and visited[ny][nx] == False:
                if grid[ny][nx] == color:
                    q.append((ny, nx))
                    visited[ny][nx] = True
    return cnt, color

def bfs_rg(stt):
    global visited, grid
    nxtColor = {}
    cnt = 0
    q = deque([stt])
    color = grid[stt[0]][stt[1]]
    visited[stt[0]][stt[1]] = True
    while len(q)>0:
        cur = q.popleft()
        cnt += 1
        for y, x in dyx:
            ny, nx = cur[0]+y, cur[1]+x
            if check((ny, nx)) == True and visited[ny][nx] == False:
                if color == 'G' or color == 'R':
                    if grid[ny][nx] != 'B':
                        q.append((ny, nx))
                        visited[ny][nx] = True
                elif color == 'B':
                    if grid[ny][nx] == color:
                        q.append((ny, nx))
                        visited[ny][nx] = True
    return cnt, color

ans = []
cnt, color = bfs((0, 0))
ans.append(cnt)

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            cnt, color = bfs((i, j))
            ans.append(cnt)

visited = [[False for _ in range(N)] for _ in range(N)]
ans1 = []
cnt, color = bfs_rg((0, 0))
ans1.append(cnt)

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            cnt, color = bfs_rg((i, j))
            ans1.append(cnt)

print(len(ans), len(ans1))