import sys
import copy
from collections import deque
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(m)]for _ in range(n)]
for i in range(n):
  arr[i] = list(map(int, sys.stdin.readline().split()))
temp = copy.deepcopy(arr)

def bfs(x,y):
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  queue=deque()
  queue.append((x,y))
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<m:
        if temp[nx][ny]==0:
          queue.append((nx,ny))
          temp[nx][ny]=2

max0 = 0
wall = list(combinations(list(range(n*m)), 3))
for i in range(len(wall)):
  x0 = wall[i][0]//m
  y0 = wall[i][0]%m
  x1 = wall[i][1]//m
  y1 = wall[i][1]%m 
  x2 = wall[i][2]//m
  y2 = wall[i][2]%m
  if(temp[x0][y0] == 0 and temp[x1][y1] == 0 and temp[x2][y2] == 0):
    temp[x0][y0] = 1
    temp[x1][y1] = 1
    temp[x2][y2] = 1
    for j in range(n):
      for k in range(m):
        if temp[j][k]==2:
          bfs(j, k)
      
    cnt = 0
    for k in range(n):
      cnt += temp[k].count(0)
    max0 = max(max0, cnt)
    if cnt>0:
      # print(x0, y0, '/', x1, y1, '/', x2, y2)
      # for k in range(n):
      #   print(temp[k])
      max0 = max(max0, cnt)
      if max0 == 31:
        break
      # print(cnt)
      # print()   
  else:
    continue
  
  temp = copy.deepcopy(arr)
print(max0)