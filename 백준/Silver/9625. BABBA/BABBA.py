k = int(input())
a = [1, 0]
for i in range(k):
    tmp = [0, 0]
    tmp[1] = a[0]
    tmp[0] = a[1]
    tmp[1] += a[1]
    a = tmp
print(a[0], a[1])