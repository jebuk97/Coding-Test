from collections import deque
def bfs(stt, grid):
    dyx = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    q = deque([(stt, 0)])
    visited[stt[0]][stt[1]] = True
    while len(q) > 0:
        cur, times = q.popleft()
        for nyx in dyx:

            ny = cur[0] + nyx[0]
            nx = cur[1] + nyx[1]
            if not (0 <= ny < len(grid) and 0<=nx<len(grid[0])):
                continue
            while True:
                if not (0 <= ny < len(grid) and 0<=nx<len(grid[0])):
                    ny = ny - nyx[0]
                    nx = nx - nyx[1]
                    break
                if grid[ny][nx] == 'D':
                    ny = ny - nyx[0]
                    nx = nx - nyx[1]
                    break
                
                ny = ny + nyx[0]
                nx = nx + nyx[1]
            
            # print(ny, nx)
            if grid[ny][nx] == 'G':
                    return times + 1
            if visited[ny][nx] == True:
                continue
            visited[ny][nx] = True
            q.append(((ny, nx), times + 1))
    return -1
def solution(board):
    grid = []
    for i in range(len(board)):
        tmp = list(board[i])
        try:
            stt = (i, tmp.index('R'))
            print(stt)
        except:
            pass
        grid.append(tmp)
    return (bfs(stt, grid))