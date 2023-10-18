n, k = map(int, input().split())
nations = [tuple(map(int, input().split())) for _ in range(n)]
nations.sort(key = lambda x: (-x[1], -x[2], -x[3]))
rank = 1
sum = 0
if n == 1:
    print(1)
else:
    for i in range(0, n-1):
        # print(rank)
        if nations[i][0] == k:
            break
        if (nations[i+1][1], nations[i+1][2], nations[i+1][3]) == (nations[i][1], nations[i][2], nations[i][3]):
            sum += 1
            pass
        else:
            rank += 1 + sum
            sum = 0
    # print(nations)
    print(rank)
