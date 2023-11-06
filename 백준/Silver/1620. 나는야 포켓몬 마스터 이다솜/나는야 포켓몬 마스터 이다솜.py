N, M = map(int, input().split())
pokemons = {}
pokekey = []
for i in range(N):
    p = input()
    pokemons[p] = i+1
    pokekey.append(p)
for _ in range(M):
    q = input()
    if q.isalpha() == True:
        print(pokemons[q])
    else:
        print(pokekey[int(q)-1])