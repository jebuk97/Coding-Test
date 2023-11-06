N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dxy = ((0, -1), (1, 0), (0, 1), (-1, 0))
turn = 0
cnt = 2
go_cnt = 0
go_max = 1
cur = (N//2, N//2)
def tornado():
    global turn, cnt, go_cnt, go_max, cur
    if cur == (0, 0):
        return
    x, y = dxy[turn%4]
    ori_cur = cur
    cur = (cur[0] + x, cur[1] + y)
    
    go_cnt += 1
    if go_cnt == go_max:
        go_cnt = 0
        turn += 1
        cnt -= 1
    if cnt == 0:
        cnt = 2
        go_max += 1
    return ori_cur, cur

def sand(x, y):
    d = dxy.index((y[0] - x[0], y[1] - x[1]))
    dx, dy = dxy[d]
    per_5 = [(y[0] + dx*2, y[1] + dy*2)]
    
    dx1, dy1 = dxy[(d+1)%4]
    dx2, dy2 = dxy[(d+3)%4]
    per_10 = [(y[0] + dx1 + dx, y[1] + dy1 + dy), (y[0] + dx2 + dx, y[1] + dy2 + dy)]
    per_7 = [(y[0] + dx1, y[1] + dy1), (y[0] + dx2, y[1] + dy2)]
    per_2 = [(y[0] + dx1*2, y[1] + dy1*2), (y[0] + dx2*2, y[1] + dy2*2)]
    per_1 = [(x[0] + dx1, x[1] + dy1), (x[0] + dx2, x[1] + dy2)]
    alpha = (y[0] + dx, y[1] + dy)
    return per_10, per_7, per_5, per_2, per_1, alpha

def debug():
    for a in A:
        print(a)
    print('====================')

ans = 0
while cur != (0, 0):
    x, y = tornado()
    per_10, per_7, per_5, per_2, per1, alpha = sand(x, y)
    percent = [per_10, per_7, per_5, per_2, per1]
    ratio = [0.1, 0.07, 0.05, 0.02, 0.01]
    if A[y[0]][y[1]] == 0:
        continue
    ori_sand = A[y[0]][y[1]]
    A[y[0]][y[1]] = 0
    sand_sum = 0
    for i, p in enumerate(percent):
        for pp in p:
            if pp[0] >= 0 and pp[0] < N and pp[1] >= 0 and pp[1] < N:
                A[pp[0]][pp[1]] += int(ratio[i]*ori_sand)
                sand_sum += int(ratio[i]*ori_sand)
            else:
                ans += int(ratio[i]*ori_sand)
                sand_sum += int(ratio[i]*ori_sand)
    if alpha[0] >= 0 and alpha[0] < N and alpha[1] >= 0 and alpha[1] < N:
        A[alpha[0]][alpha[1]] += ori_sand - sand_sum
    else:
        ans += ori_sand - sand_sum
    # debug()

print(ans)
