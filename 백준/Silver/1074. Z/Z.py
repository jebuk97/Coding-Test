import sys
N, r, c = map(int, sys.stdin.readline().split())
cnt = 0
dyx = ((0, 0), (0, 1), (1, 0), (1, 1))
def z(stt, n):
    global cnt, dyx, r, c
    if n < 1:
        # print(stt)
        if stt[0] == r and stt[1] == c:
            print(cnt)
            return
        cnt += 1
        return
    # for yx in dyx:
    #     y, x = yx
    if r < stt[0]+n and c < stt[1]+n:
        z((stt[0], stt[1]), n//2)
    elif r < stt[0]+n and c >= stt[1]+n:
        cnt += n*n
        z((stt[0], stt[1]+n), n//2)
    elif r >= stt[0]+n and c < stt[1]+n:
        cnt += n*n*2
        z((stt[0]+n, stt[1]), n//2)
    else:
        cnt += n*n*3
        z((stt[0]+n, stt[1]+n), n//2)

z((0, 0), 2**(N-1))