from collections import defaultdict
N, M = map(int, input().split())
words = defaultdict(int)
for _ in range(N):
    w = input()
    if len(w) >= M:
        words[w] += 1
k = list(words.keys())
k.sort(key=lambda x: (-words[x], -len(x), x))
for kk in k:
    print(kk)