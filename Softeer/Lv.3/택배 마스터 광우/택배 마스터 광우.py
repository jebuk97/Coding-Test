import sys
from itertools import permutations
n, m, k = map(int, sys.stdin.readline().split())
rails = list(map(int, sys.stdin.readline().split()))
ans = 99999999999
for i in permutations(rails, n):
    l = 0
    tmp = 0
    for j in range(k):
        summ = 0
        while True:
            summ += i[l%n]
            if summ > m:
                summ -= i[l%n]
                tmp += summ
                break
            l+=1
    ans = min(ans, tmp)
print(ans)