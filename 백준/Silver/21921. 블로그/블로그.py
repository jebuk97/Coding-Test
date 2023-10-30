N, X = map(int, input().split())
visitors = list(map(int, input().split()))
max_visits = 0
cnt = 0
s = sum(visitors[0:X])
max_visits = s
cnt = 1
stt = 0
end = X-1
# print(stt, end)
for i in range(0, N-X):
    s -= visitors[stt]
    stt += 1
    end += 1
    s += visitors[end]
    # print(stt, end)
    if max_visits < s:
        max_visits = s
        cnt = 1
    elif max_visits == s:
        cnt += 1
    # print(s)
if max_visits == 0:
    print('SAD')
else:
    print(max_visits)
    print(cnt)