from collections import deque
import heapq
def solution(operations):
    h = []
    maxh = []
    length = 0
    for o in operations:
        comm, num = o.split()
        if length == 0:
            h = []
            maxh = []
        if comm == 'I':
            num = int(num)
            heapq.heappush(h, num)
            heapq.heappush(maxh, -num)
            length += 1
        elif comm == 'D' and length > 0:
            length -= 1
            if num == '-1':
                heapq.heappop(h)
            elif num == '1':
                heapq.heappop(maxh)
        print(h, maxh)
    if length <= 0:
        return [0,0]
    else:
        return [-heapq.heappop(maxh),heapq.heappop(h)]
    answer = []
    return answer