switchs = int(input())
switch = list(map(int, (input().replace(" ", ""))))
n = int(input())
# print(switchs, switch, n)
for _ in range(n):
    new = [0] * switchs
    st, num = map(int, input().split())
    num -= 1
    if st == 1:
        for i in range(num, switchs, num+1):
            switch[i] ^= 1
        # print(st, switch)
    else:
        switch[num] ^= 1
        for j in range(1, min(num+1, switchs-num)):
            if switch[num-j] == switch[num+j]:
                # print(num-j, num+j)
                switch[num - j] ^= 1
                switch[num + j] ^= 1
            else:
                break
            # print(j, st, switch)
start = 0
end = 20
while True:
    if len(switch)<=end:
        print(*switch[start:])
        break
    else:
        print(*switch[start:end])
        start += 20
        end += 20