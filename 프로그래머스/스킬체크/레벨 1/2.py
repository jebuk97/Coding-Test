'''
로또 번호와 당첨 번호가 주어진다.
기억나지 않는 로또 번호는 0으로 입력된다.
최선의 등수, 최악의 등수를 출력한다.
'''

def solution(lottos, win_nums):
    best = 0
    worst = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            best += 1
        elif lottos[i] in win_nums:
            best += 1
            worst += 1

    best = 6 - best + 1
    worst = 6 - worst + 1
    if best > 6:
        best = 6
    if worst > 6:
        worst = 6

    answer = [best, worst]
    return answer