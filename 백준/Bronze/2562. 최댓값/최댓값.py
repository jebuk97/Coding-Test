maximum = 0
idx = 0
for i in range(9):
    num = int(input())
    if num > maximum:
        maximum = num
        idx = i+1
print(maximum)
print(idx)