from collections import deque
M, N, H= map(int, input().split())
tomato0 = set()
tomato1 = deque()
boxes = []
for h in range(H):
    graph = []
    for i in range(N):
        col = list(map(int, input().split()))
        for j, c in enumerate(col):
            if c == 1:
                tomato1.append((h, i, j))
            elif c == 0:
                tomato0.add((h, i, j))
        graph.append(col)
    boxes.append(graph)

DEBUG = False
if DEBUG is True:
    for b in boxes:
        for g in b:
            print(g)
def check(c):
    return 0<=c[0]<H and 0<=c[1]<N and 0<=c[2]<M

dyx = ((0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0))
def bfs():
    day = 0
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
    q = deque()
    for t in tomato1:
        q.append((t, day))
        visited[t[0]][t[1]][t[2]] = True

    while len(q) > 0:
        cur, day = q.popleft()
        ch, cy, cx = cur
        for d in dyx:
            nh, ny, nx = ch + d[0], cy + d[1], cx + d[2]
            if check((nh, ny, nx)) == True and visited[nh][ny][nx] == False and boxes[nh][ny][nx] == 0:

                tomato0.remove((nh, ny, nx))
                q.append(((nh, ny, nx), day + 1))
                boxes[nh][ny][nx] = 1
                visited[nh][ny][nx] = True
    if len(tomato0) > 0:
        return -1
    else:
        return day
print(bfs())