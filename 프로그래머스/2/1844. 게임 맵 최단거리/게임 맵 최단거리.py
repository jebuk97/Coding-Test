from collections import deque
def check(c, n, m):
    return 0<=c[0]<n and 0<=c[1]<m
def solution(maps):
    dyx = ((0, 1), (0, -1), (1, 0), (-1, 0))
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque([((0, 0), 1)])
    print(q)
    visited[0][0] = True
    while len(q) > 0:
        cur, tmp = q.popleft()
        for yx in dyx:
            nxt = (cur[0]+yx[0], cur[1]+yx[1])
            if nxt[0] == n-1 and nxt[1] == m-1:
                return tmp+1
            if check(nxt, n, m) == False:
                continue
            if visited[nxt[0]][nxt[1]] == True or maps[nxt[0]][nxt[1]] == 0:
                continue
            q.append(((nxt[0], nxt[1]), tmp+1))
            visited[nxt[0]][nxt[1]] = True
    return -1