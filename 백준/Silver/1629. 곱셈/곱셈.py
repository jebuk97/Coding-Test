import sys
a, b, c = map(int, sys.stdin.readline().split())

def mul(s):
    if s == 1:
        return a % c
    tmp = mul(s//2)
    if s % 2 == 0:
        ans = tmp * tmp % c
    else:
        ans = tmp * tmp * a % c
    return ans

print(mul(b))