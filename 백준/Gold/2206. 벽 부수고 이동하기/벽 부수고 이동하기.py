from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
def check(c):
    y, x = c
    return 0<=y<n and 0<=x<m

dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))
def bfs():
    q = deque([((0, 0), 0, False)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited1 = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    while len(q) > 0:
        # print(q)
        cur, cnt, flag = q.popleft()
        if cur == (n-1, m-1):
            return cnt+1
        for yx in dyx:
            y, x = yx
            ny, nx = cur[0] + y, cur[1] + x
            if check((ny, nx)) == False:
                continue
            if flag == False and visited[ny][nx] == False:
                if graph[ny][nx] == 0:
                   q.append(((ny, nx), cnt+1, False))
                   visited[ny][nx] = True
                else:
                    q.append(((ny, nx), cnt + 1, True))
                    visited1[ny][nx] = True
            if flag == True and visited1[ny][nx] == False:
                if graph[ny][nx] == 0:
                    q.append(((ny, nx), cnt + 1, True))
                    visited1[ny][nx] = True
                else:
                    continue

    return -1
print(bfs())
