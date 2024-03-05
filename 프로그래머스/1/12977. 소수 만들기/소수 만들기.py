from itertools import combinations
def solution(nums):
    answer = 0
    for n in combinations(nums, 3):
        odd = 0
        even = 0
        for i in range(3):
            if n[i] % 2 == 0:
                even += 1
            else:
                odd += 1
        if odd % 2 == 0:
            continue
        else:
            s = sum(n)
            flag = True
            for i in range(2, s):
                if s % i == 0:
                    flag = False
                    break
            if flag is True:
                answer += 1

    return answer