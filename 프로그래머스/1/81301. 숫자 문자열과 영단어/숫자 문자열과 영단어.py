def solution(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    i = 0
    while i < len(nums):
        try:
            idx = s.index(nums[i])
        except:
            i += 1
            continue
        s = list(s)
        s[idx] = str(i)
        for j in range(1, len(nums[i])):
            s[idx+j] = ''

        s = ''.join(s)
    answer = int(s)
    return answer