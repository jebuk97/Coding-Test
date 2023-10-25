import math
num = int(input())
start = math.ceil(num / 2)
nums = []
ans = []
sum = 0
for i in range(start, 0, -1):
    nums = [i]
    sum = i
    for j in range(i-1, 0, -1):
        # print(i, j)
        sum += j
        if sum == num:
            nums.append(j)
            ans.append(nums)
            nums = []
            sum = 0
            break
        elif sum > num:
            nums = []
            sum = 0
            break
        else:
            nums.append(j)

print(len(ans) + 1)