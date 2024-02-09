def solution(sequence, k):
    tmp = 0
    answers = []
    stt, end = 0, 0
    tmp = sequence[0]
    while stt <= end < len(sequence):
        if tmp < k:
            end += 1
            if end < len(sequence):
                tmp += sequence[end]
        elif tmp > k:
            tmp -= sequence[stt]
            stt += 1
        else:
            answers.append([stt, end])
            tmp -= sequence[stt]
            stt += 1

    answers.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answers[0]