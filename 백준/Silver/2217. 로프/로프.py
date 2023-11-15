n = int(input())
w = [int(input()) for _ in range(n)]
w.sort()
tmp = []
for i in range(n):
    tmp.append(w[i] * (n-i))
print(max(tmp))