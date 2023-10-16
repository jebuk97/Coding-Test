'''
1
2 7 5
8 19 11
20 37 17
38 61 23
'''

num = int(input())
n = 1
start = 1
end = 1
while True:
    if start<=num<=end:
        print(n)
        break
    start = end+1
    end=end+6*n
    n+=1