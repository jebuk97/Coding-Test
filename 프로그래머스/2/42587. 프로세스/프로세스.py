from queue import PriorityQueue
from collections import deque
def solution(priorities, location):
    q = deque([])
    q1 = deque(priorities)
    for i in range(len(priorities)):
        q.append((priorities[i], i))

    maxi = max(q1)
    i=0
    while len(q) > 0:
        cur, loc = q.popleft()
        tmp = q1.popleft()
        if maxi > cur:
            q.append((cur, loc))
            q1.append(tmp)
        else:
            if loc == location:
                return i+1
            maxi = max(q1)
            i += 1
    answer = 0
    return answer