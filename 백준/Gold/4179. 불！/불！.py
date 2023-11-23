from collections import deque
import sys
r, c = map(int, sys.stdin.readline().split())
fire = deque()
stt = None
maze = []
OK = []
for i in range(r):
    col = list(sys.stdin.readline().rstrip())
    for j in range(c):
        if col[j] == 'J':
            stt = (i, j)
        elif col[j] == 'F':
            fire.append((i, j))
    maze.append(col)
# for m in maze:
#     print(m)
def check(cord):
    y, x = cord
    return 0 <= y < r and 0 <= x < c

dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(stt):
    global OK
    q = deque([(stt, 0)])
    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[stt[0]][stt[1]] = True
    while len(q) > 0:
        cur, cnt = q.popleft()
        if len(OK) == cnt:
            OK.append(1)
            bfs_fire()
            # for m in maze:
            #     print(m)

        for y, x in dyx:
            ny, nx = cur[0] + y, cur[1] + x
            if check((ny, nx)) == False:
                return cnt + 1
            if maze[ny][nx] == '.' and visited[ny][nx] == False:
                q.append(((ny, nx), cnt+1))
                visited[ny][nx] = True
    return 'IMPOSSIBLE'

def bfs_fire():
    for _ in range(len(fire)):
        cur = fire.popleft()
        for y, x in dyx:
            ny, nx = cur[0] + y, cur[1] + x
            if check((ny, nx)) == False:
                continue
            if maze[ny][nx] == '.':
                fire.append((ny, nx))
                maze[ny][nx] = 'F'

# def fire()
print(bfs(stt))
