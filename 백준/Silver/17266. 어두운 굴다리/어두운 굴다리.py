import math
n = int(input())
m = int(input())
loc = list(map(int, input().split()))
# print(n, m, loc)
height = loc[0]
if loc[m-1] + height < n:
    height = n - loc[m-1]
# print(height)
maxi = 0
for i in range(len(loc)-1):
    if loc[i+1] - loc[i] <= height * 2:
        continue
    else:
        height_need = math.ceil((loc[i+1] - loc[i])/2 - height)
        if height_need > maxi:
            maxi = height_need

print(maxi + height)