import sys

N, M = map(int, sys.stdin.readline().split())
room = dict()
for _ in range(N):
    room[sys.stdin.readline().rstrip()] = []

for _ in range(M):
    name, stt, end = sys.stdin.readline().split()
    room[name].append((int(stt), int(end)))
room = dict(sorted(room.items()))
flag = False
for r in room:
    if flag == True:
        print('-----')
    else:
        flag = True
    d = sorted(room[r])
    print(f'Room {r}:')
    ans = []
    if len(d) == 0:
        ans.append('09-18')
    for i in range(len(d)):
        if i == 0:
            if d[i][0] > 9:
                ans.append(f'09-{d[i][0]}')
        else:
            if d[i - 1][1] != d[i][0]:
                ans.append(f'{d[i - 1][1]}-{d[i][0]}')
        if i == len(d) - 1:
            if d[i][1] < 18:
                ans.append(f'{d[i][1]}-18')

    if len(ans) == 0:
        print('Not available')
    else:
        print(f'{len(ans)} available:')
        for i in range(len(ans)):
            print(ans[i])