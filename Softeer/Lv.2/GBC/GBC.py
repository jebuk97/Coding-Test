import sys
n, m = map(int, sys.stdin.readline().split())
limit = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
speed = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
# print(limit)
# print(speed)
s1 = 0
s2 = 0
flag = [False for _ in range(n)]
save = [0 for _ in range(n)]
for i in range(m):
    sp = speed[i]
    s2 += sp[0]
    s1 = 0
    for j in range(n):
        s1 += limit[j][0]
        if flag[j] is True:
            continue
        if speed[i][1] > limit[j][1]:
            save[j] = max(save[j], speed[i][1] - limit[j][1])
        # print(s1, s2, save)
        if s2 >= s1:
            flag[j] = True
        if s1 >= s2:
            break
print(max(save))