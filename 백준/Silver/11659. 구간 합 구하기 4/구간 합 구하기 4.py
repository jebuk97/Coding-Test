import sys
M, N = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sums = [nums[0]]
for i in range(1, M):

    sums.append(sums[i-1]+nums[i])

for i in range(N):
    stt, end = map(int, sys.stdin.readline().split())
    if stt == 1:
        print(sums[end - 1])
    else:
        print(sums[end - 1] - sums[stt - 2])