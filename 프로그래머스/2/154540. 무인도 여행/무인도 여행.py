from collections import deque
def bfs(grid, stt, visited):
    dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))
    q = deque([stt])
    visited[stt[0]][stt[1]] = True
    s = 0
    while len(q) > 0:
        cur = q.popleft()
        s += int(grid[cur[0]][cur[1]])
        for d in dyx:
            # print(cur, d)
            ny, nx = (cur[0] + d[0], cur[1] + d[1])
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] != 'X' and visited[ny][nx] is False:
                q.append((ny, nx))
                visited[ny][nx] = True
            
    return s, grid, visited
def solution(maps):
    
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    grid = []
    answer = []
    summ = -1
    for m in maps:
        grid.append(list(m))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            if visited[i][j] is True or grid[i][j] == 'X':
                continue
            else:
                summ, grid, visited = bfs(grid, (i, j), visited)
                answer.append(summ)
    if len(answer) == 0:
        return [-1]
    return sorted(answer)
