n = int(input())
grid = [input() for _ in range(n)]
left_arm = 0
right_arm = 0
back = 0
left_leg = 0
right_leg = 0
head = -1
check_arm = False
check_leg = -1
heart_idx = 0
for i, g in enumerate(grid):
    if head == -1:
        head = g.find('*')
    elif head != -1 and check_arm == False:
        heart_idx = i
        left_arm = g.find('*')
        left_arm = head - left_arm
        for j in range(head+1, n):
            if g[j] == '*':
                right_arm += 1
            else:
                break
        check_arm = True
        continue
    elif head != -1 and check_arm == True:
        if g[head] == '*':
            back += 1
            continue
        else:
            if check_leg == -1:
                check_leg = g.index('*')
            if g[check_leg] == '*':
                left_leg += 1
            if g[check_leg + 2] == '*':
                right_leg += 1
    else: continue
print(heart_idx + 1, head + 1)
print(left_arm, right_arm, back, left_leg, right_leg)