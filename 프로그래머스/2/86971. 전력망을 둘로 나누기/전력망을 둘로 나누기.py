from collections import deque
def bfs(grid, n, stt):
    visited = [False for _ in range(n+1)]
    visited[stt] = True
    q = deque([stt])
    num = 1
    while len(q)>0:
        cur = q.popleft()
        for n in grid[cur]:
            if visited[n] is False:
                num += 1
                visited[n] = True
                q.append(n)
    return num
def solution(n, wires):
    answer = 999
    grid = {}
    
    for i in range(len(wires)):
        for k in range(1, n+1):
            grid[k]=[]
        for j in range(len(wires)):
            if i==j:
                continue
            else:
                grid[wires[j][0]].append(wires[j][1])
                grid[wires[j][1]].append(wires[j][0])
        # print(wires[i])
        answer = min(answer, abs(bfs(grid, n, wires[i][0])-bfs(grid, n, wires[i][1])))
    return answer