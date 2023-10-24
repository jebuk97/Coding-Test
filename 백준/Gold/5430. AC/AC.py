from collections import deque
T = int(input())

def debug():
    print(func, n)
    print(arr)
    print('=========')

for t in range(T):
    func = input()
    n = int(input())
    arr = input()
    if n > 0:
        arr = arr[1:len(arr)-1]
        arr = arr.replace('RR', '')
        arr = deque(arr.split(','))
    else:
        arr = deque()
    # print(func)
    # debug()

    func = deque(func)
    err = False
    rev = 0
    while len(func) > 0:
        cur = func.popleft()
        # print(arr, len(arr))
        if cur == 'R':
           rev = (rev + 1) % 2
        else:
            if len(arr) == 0:
                err = True
                break
            else:
                if rev == 0:
                    arr.popleft()
                elif rev == 1:
                    arr.pop()
    if err:
        print('error')
    else:
        if rev == 1:
            arr.reverse()
        print(f"[{(','.join(arr))}]")