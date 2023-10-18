n, new_p, p = map(int, input().split())
rank = 1
if n == 0:
    print(1)
else:
    ps = list(map(int, input().split()))
    if ps[len(ps)-1] >= new_p and len(ps) == p:
        print(-1)
    else:
        for i, pp in enumerate(ps):
            if pp > new_p:
                rank += 1
            else:
                break
        print(rank)