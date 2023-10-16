mo = {'a', 'e', 'i', 'o', 'u'}
def r1(s):
    global mo
    for i in range(len(s)):
        if s[i] in mo:
            return True
    return False
def r2(s):
    global mo
    if len(s) < 3:
        return True
    for i in range(2, len(s)):
        if s[i-2] in mo and s[i] in mo and s[i-1] in mo:
            return False
        if s[i-2] not in mo and s[i] not in mo and s[i-1] not in mo:
            return False
    return True
def r3(s):
    if len(s) == 1:
        return True
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            if s[i-1] == 'e' or s[i-1] == 'o':
                continue
            else: return False
    return True

while True:
    s = input()
    if s == 'end':
        break
    # print(r1(s), r2(s), r3(s))
    if r1(s) is True and r2(s) is True and r3(s) is True:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')