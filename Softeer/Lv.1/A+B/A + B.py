import sys
T = int(sys.stdin.readline().rstrip())
for t in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{t+1}: {a+b}')