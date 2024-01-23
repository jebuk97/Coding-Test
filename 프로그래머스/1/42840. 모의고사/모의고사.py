def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4 ,2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            cnt[0] += 1
        if answers[i] == two[i%len(two)]:
            cnt[1] += 1
        if answers[i] == three[i%len(three)]:
            cnt[2] += 1
    maxi = max(cnt)
    
    answer = []
    for i in range(len(cnt)):
        if cnt[i] == maxi:
            answer.append(i+1)
    print(cnt)
    answer.sort()
    return answer