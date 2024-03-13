def solution(num, total):
    first = 1
    second = num + 1
    while True:
        tmp = 0
        for i in range(first, second):
            tmp += i
        if tmp < total:
            first += 1
            second += 1
        elif tmp > total:
            first -= 1
            second -= 1
        else:
            break
    answer = []
    for i in range(first, second):
        answer.append(i)
    return answer