from collections import deque
M, N = map(int, input().split())
tomato0 = set()
tomato1 = deque()
graph = []
for i in range(N):
    col = list(map(int, input().split()))
    for j, c in enumerate(col):
        if c == 1:
            tomato1.append((i, j))
        elif c == 0:
            tomato0.add((i, j))
    graph.append(col)

def check(c):
    return 0<=c[0]<N and 0<=c[1]<M

dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))
def bfs():
    day = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    day = 0
    q = deque()
    for t in tomato1:
        q.append((t, day))
        visited[t[0]][t[1]] = True

    while len(q) > 0:
        cur, day = q.popleft()
        cy, cx = cur
        for d in dyx:
            ny, nx = cy + d[0], cx + d[1]
            if check((ny, nx)) == True and visited[ny][nx] == False and graph[ny][nx] == 0:

                tomato0.remove((ny, nx))
                q.append(((ny, nx), day + 1))
                graph[ny][nx] = 1
                visited[ny][nx] = True
    if len(tomato0) > 0:
        return -1
    else:
        return day
print(bfs())