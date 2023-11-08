import sys
S = set()
n = int(sys.stdin.readline())
#
for _ in range(n):
    com = list(sys.stdin.readline().split())
    if 'add' == com[0]:
        S.add(int(com[1]))
    elif 'remove' == com[0]:
        S.discard(int(com[1]))
    elif 'check' == com[0]:
        if int(com[1]) in S:
            print(1)
        else:
            print(0)
    elif 'toggle' == com[0]:
        num = int(com[1])
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif 'all' == com[0]:
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    else:
        S = set()