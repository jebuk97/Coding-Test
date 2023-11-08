import sys
N = int(sys.stdin.readline())
times = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
times.sort(key = lambda x: (x[1], x[0]))
meets = 1
end = times[0][1]
for i in range(N-1):
    if end <= times[i+1][0]:
        meets += 1
        end = times[i+1][1]
print(meets)