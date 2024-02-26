def solution(n, arr1, arr2):
    
    answer = [[] for _ in range(n)]
    for i in range(n):
        a = (str(bin(arr1[i]))[2:].zfill(n))
        b = (str(bin(arr2[i]))[2:].zfill(n))
        for j in range(n):
            if a[j] == '1' or b[j] == "1":
                answer[i].append('#')
            else:
                answer[i].append(' ')
        answer[i] = ''.join(answer[i])    
    return answer