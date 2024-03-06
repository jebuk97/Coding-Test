def recur(arr, n, y, x):
    if n == 1:
        return arr
    
    
    one = 0
    zero = 0
    for yx in ((y, x), (y, x+n), (y+n, x), (y+n, x+n)):
        flag = False
        ny, nx = yx
        # print(ny, nx, '-', ny+n-1, nx+n-1)
        for i in range(ny, ny+n):
            if flag is True:
                break
            for j in range(nx, nx+n):
                if arr[i][j] != 0 and arr[i][j] != 1:
                    continue
                if arr[i][j] != arr[ny][nx]:
                    # print('not same')
                    flag = True
                    break
        if flag is False:
            # print('same')
            for i in range(ny, ny+n):
                for j in range(nx, nx+n):
                    if i == ny and j == nx:
                        continue
                    else:
                        arr[i][j] = 2
    recur(arr, n//2, y, x)
    recur(arr, n//2, y, x+n)
    recur(arr, n//2, y+n, x)
    recur(arr, n//2, y+n, x+n)
    
    

def solution(arr):
    flag = False
    for i in range(len(arr)):
        if flag is True:
            break
        for j in range(len(arr)):
            if arr[i][j] != arr[0][0]:
                flag = True
                break
    
    if flag is True:
        
        answer = [0, 0]
        recur(arr, len(arr)//2, 0, 0)

        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] == 0:
                    answer[0] += 1
                elif arr[i][j] == 1:
                    answer[1] += 1
    else:
        if arr[0][0] == 0:
            return [1, 0]
        else:
            return [0, 1]
                    
    return answer