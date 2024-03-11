from collections import deque
def solution(n, s, a, b, fares):
    fare_graph = [[99999999999 for _ in range(n)] for _ in range(n)]
    neighbors = [[] for _ in range(n)]
    for f in fares:
        fare_graph[f[0] - 1][f[1] - 1] = f[2]
        fare_graph[f[1] - 1][f[0] - 1] = f[2]
        neighbors[f[0] - 1].append(f[1])
        neighbors[f[1] - 1].append(f[0])
    dists = {}
    for node in range(1, n+1):
        visited = [False for _ in range(n)]
        dist = [99999999999 for _ in range(n)]
        dist[node - 1] = 0
        q = deque([(0, node)])
        visited[node - 1] = True
        while len(q) > 0:
            d, cur = q.popleft()
            if dist[cur-1] < d:
                continue
            nxt = neighbors[cur - 1]
            for nn in nxt:
                new_dist = dist[cur - 1] + fare_graph[cur - 1][nn - 1]
                if new_dist < dist[nn-1]:
                    dist[nn-1] = new_dist
                    q.append((new_dist, nn))
        dists[node] = dist

    answer = 99999999999
    # print(dists)
    for i in range(1, n+1):
        answer = min(answer, dists[s][i-1] + dists[i][a-1] + dists[i][b-1])
    return answer