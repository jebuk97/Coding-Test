N, K = map(int, input().split())
nums = [i for i in range(1, N+1)]
point = K-1
ans = []

for i in range(N):
    # print(nums)
    ans.append(str(nums.pop(point)))
    if len(nums) == 0:
        break
    point = (point + K-1) % len(nums)

if len(ans) == 1:
    print('<'+ans[0]+'>')
else:
    ansstr = '<'+ans[0]+', '
    for i in range(1, N-1):
        ansstr += ans[i]+', '
    ansstr += ans[N-1]+'>'
    print(ansstr)