from collections import defaultdict, deque
import math
def solution(fees, records):
    dict_in = {}
    dict_out = {}
    fee = defaultdict(int)
    for r in records:
        tmp = r.split()
        time = tmp[0].split(':')
        if tmp[2] == 'IN':
            try:
                dict_in[tmp[1]].append(int(time[0]) * 60 + int(time[1]))
            except:
                dict_in[tmp[1]] = deque([(int(time[0]) * 60 + int(time[1]))])
        if tmp[2] == 'OUT':
            try:
                dict_out[tmp[1]].append(int(time[0]) * 60 + int(time[1]))
            except:
                dict_out[tmp[1]] = deque([(int(time[0]) * 60 + int(time[1]))])
    for d in dict_in:
        while len(dict_in[d]) > 0:
            try:
                fee[d] += dict_out[d].popleft() - dict_in[d].popleft()
            except:
                fee[d] += 24*60 - dict_in[d].popleft() - 1
    fee = sorted(fee.items())
    answer = []
    # print(fee)
    for f in fee:
        if f[1] <= fees[0]:
            answer.append(fees[1])
        else:
            tmp = fees[1] + math.ceil((f[1] - fees[0]) / fees[2]) * fees[3]
            answer.append(tmp)
    # print(answer)
    return answer