while True:
    one, two, three = map(int, input().split())
    side = [one, two, three]
    if one == 0 and two == 0 and three == 0:
        break
    maxi = side.pop(side.index(max(side)))
    if maxi ** 2 == side[0]**2 + side[1] ** 2:
        print('right')
    else:
        print('wrong')