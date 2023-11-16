from collections import deque
import sys
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    stt, end = map(int, sys.stdin.readline().split())
    graph[stt].append(end)
    graph[end].append(stt)
def bfs():
    visited = [-1 for _ in range(n+1)]
    q = deque([1])
    visited[1] = 0
    while len(q) > 0:
        nxt = q.popleft()
        for i in graph[nxt]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = nxt
    return visited
ans = bfs()
for i in range(2, n+1):
    print(ans[i])