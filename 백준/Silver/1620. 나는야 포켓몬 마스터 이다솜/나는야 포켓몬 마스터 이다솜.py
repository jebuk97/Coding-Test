import sys
N, M = map(int, sys.stdin.readline().strip().split())
pokemons = {}
pokekey = []
for i in range(N):
    p = sys.stdin.readline().strip()
    pokemons[p] = i+1
    pokekey.append(p)
for _ in range(M):
    q = sys.stdin.readline().strip()
    if q.isalpha() == True:
        print(pokemons[q])
    else:
        print(pokekey[int(q)-1])