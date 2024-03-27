def hanoi(move, stt, dest, mid, answer):
    if move == 1:
        answer.append([stt, dest])
        return
    hanoi(move-1, stt, mid, dest, answer)
    answer.append([stt, dest])
    hanoi(move-1, mid, dest, stt, answer)
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer