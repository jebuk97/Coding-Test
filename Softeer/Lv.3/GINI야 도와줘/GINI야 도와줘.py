import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())

grid = []
rain = []
for i in range(r):
    tmp = list(sys.stdin.readline().strip())
    for t in range(c):
        if tmp[t] == 'W':
            wash = (i, t)
        elif tmp[t] == '*':
            rain.append((i, t))

    grid.append(tmp)

dyx = ((-1, 0), (1, 0), (0, -1), (0, 1))


def check(y, x):
    return 0 <= y < r and 0 <= x < c


def bfs():
    q = deque(rain)
    q.append((wash[0], wash[1], 0))
    while len(q) > 0:
        tmp = q.popleft()
        if len(tmp) == 2:
            mode = 'rain'
            cur = tmp
        else:
            mode = 'tae'
            cur = [0, 0]
            cur[0], cur[1], dist = tmp
        for yx in dyx:
            y, x = yx
            ny, nx = cur[0] + y, cur[1] + x
            if mode == 'rain':
                if check(ny, nx) == True:
                    if grid[ny][nx] == '.' or grid[ny][nx] == 'V':
                        q.append((ny, nx))
                        grid[ny][nx] = '*'

            else:
                if check(ny, nx) == True:
                    if grid[ny][nx] == 'H':
                        return dist + 1
                    if grid[ny][nx] == '.':
                        q.append((ny, nx, dist + 1))
                        grid[ny][nx] = 'V'

        # for g in grid:
        #     print(g)
        # print()
    return 'FAIL'


print(bfs())