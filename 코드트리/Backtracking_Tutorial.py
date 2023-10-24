n, k = map(int, input().split())
grid = [[0]*n for _ in range(n)]
cur = (0, 0)
for i in range(k):
    direction, move = input().split()
    move = int(move)
    if direction == 'S':
        y, x = cur
        for m in range(move):
            y += 1
            grid[y][x] += 1
        cur = (y, x)
    elif direction == 'E':
        y, x = cur
        for m in range(move):
            x += 1
            grid[y][x] += 1
        cur = (y, x)
    elif direction == 'W':
        y, x = cur
        for m in range(move):
            x -= 1
            grid[y][x] += 1
        cur = (y, x)
    elif direction == 'N':
        y, x = cur
        for m in range(move):
            y -= 1
            grid[y][x] += 1
        cur = (y, x)

    # print(cur)
for g in grid:
    print(*g)