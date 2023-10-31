from collections import deque

q = deque(list(input().rstrip()))
n = 1
while len(q) > 0:
    # print(q)
    for s in str(n):
        if len(q) > 0 and q[0] == s:
            q.popleft()
    n += 1
print(n-1)