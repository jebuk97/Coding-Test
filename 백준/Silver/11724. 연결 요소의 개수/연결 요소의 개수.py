from collections import deque
N, M = map(int, input().split())
graph = [set() for _ in range(N)]

def bfs():
    visited = [False for _ in range(N)]
    comps = 0
    for i in range(N):
        if visited[i] == True:
            continue
        q = deque([i])
        visited[i] = True
        cnt = -1
        while len(q) > 0:
            cur = q.popleft()
            cnt += 1
            for nxt in graph[cur]:
                if visited[nxt] == False:
                        q.append(nxt)
                        visited[nxt] = True
        if cnt > -1:
            comps += 1
    return comps
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    graph[i].add(j)
    graph[j].add(i)
# print(graph)
print(bfs())