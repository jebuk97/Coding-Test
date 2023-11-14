import itertools
from collections import Counter
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
c = Counter()
ans = []
for i in itertools.permutations(nums, m):
    ans.append(i)
for j in list(Counter(ans).keys()):
    print(*j)