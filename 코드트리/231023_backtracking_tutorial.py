answer = []
K, N = map(int, input().split())
def choose():
    if len(answer) == N: #자리수
        print(*answer)
        return
    for i in range(K): #들어갈 순열
        answer.append(i+1)
        choose()
        answer.pop()
    return
choose()
'''
1 1
1 2
2 1
2 2
'''