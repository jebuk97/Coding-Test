from collections import deque
n = int(input())
grid = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    grid[r-1][c-1] = 1
rotate = deque()
l = int(input())
for _ in range(l):
    rotate.append(tuple(input().split()))

snake = deque()
snake.append((0, 0))

def debug():
    for g in grid:
        print(g)
    print(snake)
    print(rotate)

def check(c):
    y, x = c
    return 0<=y<n and 0<=x<n
dyx = ((0, 1), (1, 0), (0, -1), (-1, 0))
cur_rot = 0

# debug()
sec = 1
while True:
    cur = snake[len(snake)-1]
    dy, dx = dyx[cur_rot]
    ny, nx = cur[0] + dy, cur[1] + dx
    if (ny, nx) in snake or check((ny, nx)) == False:
        break
    snake.append((ny, nx))
    if grid[ny][nx] == 1:
        grid[ny][nx] = 0
    else:
        snake.popleft()

    if len(rotate) > 0:
        if rotate[0][0] == str(sec):
            c = rotate.popleft()
            if c[1] == 'D':
                cur_rot = (cur_rot+1) % 4
            else:
                cur_rot = (cur_rot-1) % 4
    # debug()
    sec += 1
print(sec)