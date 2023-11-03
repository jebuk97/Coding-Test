N = int(input())
time = (list(map(int, input().split())))
time.sort()
total = 0
for i in range(N):
  total += sum(time[0:i+1])
print(total)