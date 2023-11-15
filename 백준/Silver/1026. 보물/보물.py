n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
A.sort()
B.sort(reverse=True)
for i in range(n):
    ans += A[i]*B[i]
print(ans)