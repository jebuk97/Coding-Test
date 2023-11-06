N = int(input())
student = [list() for _ in range(N**2)]
order = []
desk = [[None for _ in range(N)] for _ in range(N)]
for i in range(N**2):
    l = list(map(int, input().split()))
    order.append(l[0]-1)
    student[l[0]-1] = set(l[1:])

dxy = ((-1, 0), (0, -1), (0, 1), (1, 0))

def check(c):
    return 0 <= c[0] < N and 0 <= c[1] < N 

def search_likes(st):
    maxList = []
    max = 0
    for i in range(N):
        for j in range(N):
            if desk[i][j] is not None:
                continue
            cnt = 0
            for y, x in dxy:
                nxt = (i + y, j + x)
                if check(nxt) == False:
                    continue
                if desk[nxt[0]][nxt[1]] in student[st]:
                    cnt += 1
            if cnt > max:
                max = cnt
                maxList = [(i, j)]
            elif cnt == max:
                maxList.append((i, j))  
    return maxList

def search_empty(likes):
    max = 0
    maxList = []
    for l in likes:
        cnt = 0
        for y, x in dxy:
            nxt = (l[0] + y, l[1] + x)
            if check(nxt) == False:
                continue
            if desk[nxt[0]][nxt[1]] is None:
                cnt += 1
        if cnt > max:
            max = cnt
            maxList = [l]
        elif cnt == max:
            maxList.append(l)
    return maxList

def satisfy():
    score = (0, 1, 10, 100, 1000)
    ans = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for y, x in dxy:
                nxt = (i + y, j + x)
                if check(nxt) == False:
                    continue
                if desk[nxt[0]][nxt[1]] in student[desk[i][j]-1]:
                    cnt += 1
            ans += score[cnt]
    return ans
            
DEBUG = False


for o in order:
    likes = search_likes(o)
    if len(likes) == 1:
        cur = likes[0]
        desk[likes[0][0]][likes[0][1]] = o + 1
    else:
        emptys = search_empty(likes)
        emptys.sort(key = lambda x: (x[0], x[1]))
        cur = emptys[0]
        desk[cur[0]][cur[1]] = o + 1
    
    if DEBUG:
        for d in desk:
            print(d)
        print('-------------')
print(satisfy())
