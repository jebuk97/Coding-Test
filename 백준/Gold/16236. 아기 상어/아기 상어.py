from collections import deque
N = int(input())
grid = []
fish = []
sizes = []
sec = 0
for i in range(N):
    col = list(map(int, input().split()))
    grid.append(col)
    for j, c in enumerate(col):
        if c == 9:
            grid[i][j] = 0
            shark = (i, j)
        elif c != 0:
            fish.append((i, j))

# for g in grid:
#     print(g)
# print(fish)

def check(c):
    y, x = c
    return 0<=y<N and 0<=x<N

dyx = ((-1, 0), (0, -1), (0, 1), (1, 0))
size = 2
eat = size
def bfs():
    global size, eat, shark, sec
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque([(shark, 0)])
    visited[shark[0]][shark[1]] = True
    ans = []
    mini = 99999
    while len(q)>0:
        cur, cnt = q.popleft()
        if grid[cur[0]][cur[1]] < size and grid[cur[0]][cur[1]] != 0:
            if cnt < mini:
                ans = [cur]
                mini = cnt
            elif cnt == mini:
                ans.append(cur)
        for yx in dyx:
            y, x = yx
            nxt = (cur[0] + y, cur[1] + x)
            if check(nxt) == True and visited[nxt[0]][nxt[1]] == False and grid[nxt[0]][nxt[1]] <= size:
                q.append((nxt, cnt+1))
                visited[nxt[0]][nxt[1]] = True
    return ans, mini
if len(fish) == 0:
    pass
else:
    while True:
        target, cnt = bfs()
        if len(target) == 0:
            break
        sec += cnt
        target.sort(key = lambda x: (x[0], x[1]))
        t = target[0]
        grid[t[0]][t[1]] = 0
        shark = t
        eat -= 1
        if eat == 0:
            size += 1
            eat = size

print(sec)