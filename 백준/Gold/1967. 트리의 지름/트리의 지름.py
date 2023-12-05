n = int(input())
if n == 1:
    print(0)
else:
    node = {}
    vertex = {}
    start = 0
    tmp = 0
    stt = 0
    for i in range(1, n+1):
        node[i] = []
        vertex[i] = []

    for i in range(n-1):
        a, b, c = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
        vertex[a].append(c)
        vertex[b].append(c)

    def dfs(stt):
        s = [(stt, 0)]
        visited = [False for _ in range(n+1)]
        maxi = 0
        ret = 0
        while len(s) > 0:
            cur, cnt = s.pop()
            if visited[cur] == True:
                continue
            visited[cur] = True
            for i in range(len(node[cur])):
                if visited[node[cur][i]] == True:
                    continue
                s.append((node[cur][i], cnt+vertex[cur][i]))
                if cnt+vertex[cur][i] > maxi:
                    maxi = cnt+vertex[cur][i]
                    ret = node[cur][i]
        return ret, maxi

    stt = dfs(1)[0]
    print(dfs(stt)[1])