from collections import defaultdict
def solution(id_list, report, k):
    report_to = {}
    report_from = {}
    for i in id_list:
        report_to[i] = set()
        report_from[i] = set()
    for r in report:
        fr, to = r.split()
        report_to[to].add(fr)
        report_from[fr].add(to)
    stop_list = set()
    for rt_id, rt in report_to.items():
        if len(rt) >= k:
            stop_list.add(rt_id)
    answer = []
    for rf_id, rf in report_from.items():
        answer.append(len(rf & stop_list))
    
    return answer