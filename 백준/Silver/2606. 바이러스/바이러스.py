from collections import deque
N = int(input())
M = int(input())
graph = [set() for _ in range(N)]

def bfs():
    visited = [False for _ in range(N)]
    q = deque([0])
    visited[0] = True
    cnt = -1
    while len(q) > 0:
        cur = q.popleft()
        cnt += 1
        for nxt in graph[cur]:
            if visited[nxt] == False:
                    q.append(nxt)
                    visited[nxt] = True
    return cnt
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    graph[i].add(j)
    graph[j].add(i)
# print(graph)
print(bfs())