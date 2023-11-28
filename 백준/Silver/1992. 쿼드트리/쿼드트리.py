import sys
n = int(sys.stdin.readline().rstrip())
vid = [list(input()) for _ in range(n)]

def comp(y, x, s):
    if s < 1:
        return vid[y][x]

    else:
        tmp = ''
        tmp+=comp(y, x, s // 2)
        tmp+=comp(y, x + s, s // 2)
        tmp+=comp(y + s, x, s // 2)
        tmp+=comp(y + s, x + s, s // 2)
        for t in tmp:
            if t != tmp[0]:
                return '('+tmp+')'
        return vid[y][x]

print(comp(0, 0, n//2))