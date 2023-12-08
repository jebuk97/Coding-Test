from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dyx = ((0, 1), (1, 1), (1, 0))
def check(c):
    return 0<=c[0]<n and 0<=c[1]<n
def dfs():
    cnt = 0
    q = deque([((0, 1), 0)])
    # visited = [[False for _ in range(n)] for _ in range(n)]
    while len(q) > 0:
        cur, direc = q.pop()
        if cur[0] == n-1 and cur[1] == n-1:
            cnt += 1
            continue
        for i in range(len(dyx)):
            if direc == 0 and i==2:
                continue
            if direc == 2 and i==0:
                continue
            ny = dyx[i][0] + cur[0]
            nx = dyx[i][1] + cur[1]
            if check((ny, nx)) == False:
                continue
            if i == 1:
                if graph[ny-1][nx] == 1 or graph[ny][nx-1] == 1:
                    continue
            if graph[ny][nx] == 1:
                continue

            # if visited[ny][nx] == False:
            q.append(((ny, nx), i))
                # visited[ny][nx] = True
                # if i == 1:
                #     visited[cur[0]][cur[1]+1] = True
                #     visited[cur[0]+1][cur[1]] = True

    return cnt
print(dfs())