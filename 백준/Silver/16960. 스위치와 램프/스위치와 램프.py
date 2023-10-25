N, M = map(int, input().split())
switch = [list(map(int, input().split()))[1:] for _ in range(N)]
light = [0] * M
for s in switch:
    for ss in s:
        light[ss-1] += 1
flag = 1
#없어도 되는 놈을 찾자 == 이 스위치가 일을 안해도 전부 켜진다
for i in range(N):
    flag = 1
    for j, s in enumerate(switch[i]):
        if light[s-1] - 1 == 0:
            flag = 0
            break
    if flag == 1:
        print(1)
        break
if flag == 0:
    print(0)