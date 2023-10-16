import math
h, w, n, m = map(int, input().split())
#5, 4 y, x

width = math.ceil(h / (n+1))
height = math.ceil(w / (m+1))

print(width * height)