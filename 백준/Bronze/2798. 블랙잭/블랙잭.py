answer = []
N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
def choose():
    global ans
    if len(answer) == 3:
        summ = sum(answer)
        if sum(answer) <= M and summ > ans:
            ans = summ
            # print(*answer)
        return
    for i in nums:
        if i in answer:
            continue
        answer.append(i)
        choose()
        answer.pop()
    return
choose()
print(ans)