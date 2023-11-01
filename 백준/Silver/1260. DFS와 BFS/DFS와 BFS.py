from collections import deque
def bfs(v):
    route = []
    visited = [False]*N
    q = deque()
    q.append(v)
    visited[v] = True
    while len(q)>0:
        cur = q.popleft()
        route.append(cur+1)
        graph[cur].sort()
        for c in graph[cur]:
            if visited[c] != True:
                q.append(c)
                visited[c] = True
    return route
def dfs(v):
    route = []
    visited = [False] * N
    q = deque()
    q.append(v)
    while len(q) > 0:
        cur = q.pop()
        if visited[cur] == True:
            continue
        visited[cur] = True
        route.append(cur+1)
        graph[cur].sort(reverse=True)
        for c in graph[cur]:
            if visited[c] != True:
                q.append(c)
    return route

N, M, V = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    #graph[stt][des]
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    graph[i].append(j)
    graph[j].append(i)

print(*dfs(V-1))
print(*bfs(V-1))