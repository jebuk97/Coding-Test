from collections import deque
def solution(elements):
    summ = set()
    for i in range(1, len(elements)+1):
        q = deque()
        for k in range(i):
            q.append(elements[k])
        summ.add(sum(q))
        for j in range(i, len(elements)+i-1):
            q.popleft()
            q.append(elements[(j)%(len(elements))])
            summ.add(sum(q))
    answer = len(summ)
    return answer