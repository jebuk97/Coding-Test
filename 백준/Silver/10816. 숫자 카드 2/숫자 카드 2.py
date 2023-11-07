from collections import Counter
input()
c = Counter(list(map(int, input().split())))
counts = []
input()
target = list(map(int, input().split()))
for t in target:
    counts.append(c[t])
print(*counts)