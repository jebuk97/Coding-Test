def solution(wallpaper):
    start = True
    luy = 999999999999
    rdy = 0
    rdx = 0
    for i, w in enumerate(wallpaper):
        revW = ''.join(reversed(w))
        # print(revW)
        try:
            idx =  w.index('#')
            revIdx = revW.index('#')
            luy = min(luy, idx)
            if len(w) - idx - 1 == revIdx:
                rdy = max(rdy, idx)
            else:
                rdy = max(rdy, len(w) - revIdx - 1)
            if start:
                lux = i
                rdx = i+1
                start = False
            else:
                rdx = i+1
        except:
            if start is False:
                continue
    # print(lux, luy, rdx, rdy)
    answer = [lux, luy, rdx, rdy+1]
    return answer