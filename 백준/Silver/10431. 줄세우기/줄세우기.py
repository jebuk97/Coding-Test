P = int(input())

for i in range(P):
    st = list(map(int, input().split()))
    n = st[0]
    st = st[1:]
    sum = 0
    for j in range(0, len(st)):
        idx = -1
        for k in range(0, j):
            if st[k] > st[j] and idx == -1:
                idx = k
        if idx != -1:
            tmp = st[j]
            for l in range(j, idx, -1):
                st[l] = st[l-1]
                sum +=1
            st[idx] = tmp
    print(n, sum)