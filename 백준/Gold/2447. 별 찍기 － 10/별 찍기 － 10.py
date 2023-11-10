def stars(n):
    arr = []
    if n == 1:
        return '*'
    Stars = stars(n//3)
    for S in Stars:
        arr.append(S*3)
    for S in Stars:
        arr.append(S+' '*(n//3)+S)
    for S in Stars:
        arr.append(S*3)
    return arr
    
n = int(input())
print('\n'.join(stars(n)))