import sys
times = [list(input().split()) for _ in range(5)]
ans = 0
for t in times:
    stt_h, stt_m = map(int, t[0].split(':'))
    end_h, end_m = map(int, t[1].split(':'))
    ans += (end_h - stt_h) * 60 + end_m - stt_m
print(ans)