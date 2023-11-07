N, M = map(int, input().split())
hear = set()
all = []
num = 0
for _ in range(N):
    hear.add(input())
for _ in range(M):
    l = input()
    if l in hear:
        all.append(l)
        num += 1
all.sort()
print(num)
for a in all:
    print(a)