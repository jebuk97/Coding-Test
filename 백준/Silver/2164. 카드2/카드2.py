import sys 
from collections import deque

num = int(sys.stdin.readline())
queue = deque()
for i in range(num):
  queue.append(i+1)
while 1:
  if len(queue) == 1:
    break
  queue.popleft()
  temp = queue.popleft()
  queue.append(temp)
print(queue.pop())