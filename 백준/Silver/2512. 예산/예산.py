N = int(input())
reqs = list(map(int, input().split()))
reqs.sort()
bud = int(input())

l = 0
r = reqs[N-1]+1
# print(reqs)
while l < r:
    mid = (l+r)//2
    # print(l, mid, r)
    maxi = 0
    for re in reqs:
        maxi += min(re, mid)

    if maxi <= bud:
        l = mid+1
    else:
        r = mid
    # print(l, r)
print(r-1)