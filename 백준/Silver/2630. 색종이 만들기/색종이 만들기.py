import sys
sys.setrecursionlimit(10**6)

num = int(input())
grid = [list(map(int, input().split())) for _ in range(num)]

white = 0
blue = 0
def devide(stt, n):
    global grid, blue, white
    if n == 1:
        if grid[stt[0]][stt[1]] == 1:
            blue += 1
        elif grid[stt[0]][stt[1]] == 0:
            white += 1
        return 
    cnt = 0
    tmp_grid = []
    for i in range(n):
        tmp_grid.append(grid[stt[0]+i][stt[1]:stt[1]+n])
    if is_one(grid[stt[0]][stt[1]], tmp_grid) is True:
        # print(grid[stt[0]][stt[1]], tmp_grid)
        # for i in range(n):
        #     print(*grid[stt[0]+i][stt[1]:stt[1]+n])
        # print('--')
        if grid[stt[0]][stt[1]] == 1:
            blue += 1
        elif grid[stt[0]][stt[1]] == 0:
            white += 1
        return
    devide(stt, n//2)
    devide((stt[0], stt[1]+n//2), n//2)
    devide((stt[0]+n//2, stt[1]), n//2)
    devide((stt[0]+n//2, stt[1]+n//2), n//2)
    return

def is_one(target, arr):
    for g in arr:
        for gg in g:
            if gg != target:
                return False
    return True

cnt = 0
if is_one(grid[0][0], grid):
    if grid[0][0] == 1:
        blue += 1
    elif grid[0][0] == 0:
        white += 1
else:
    devide((0, 0), num)
print(white)
print(blue)