import sys
sys.setrecursionlimit(100000)

def recur(tri, stt, n, end, num):
    if num > end:
        return tri
    for i in range(stt*2, n):
        tri[i][stt] = num
        num += 1
        if num > end:
            return tri
    for j in range(stt+1, n-stt):
        tri[i][j] = num
        num += 1
        if num > end:
            return tri
    for k in range(n-2, stt*2, -1):
        tri[k][len(tri[k])-stt-1] = num
        num += 1
        if num > end:
            return tri
    
    recur(tri, stt+1, n-1, end, num)
def solution(n):
    tri = [[0] *(i+1) for i in range(n)]
    num = 1
    end = 0
    for i in range(n):
        end+=i+1
    recur(tri, 0, n, end, num)
    # for t in tri:
    #     print(t)
    answer = []
    for t in tri:
        answer += t
    return answer