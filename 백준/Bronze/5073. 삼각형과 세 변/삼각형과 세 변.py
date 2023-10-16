while True:
   tri = list(map(int, input().split()))
   if tri[0] == 0 and tri[1] == 0 and tri[2] == 0:
       break
   longest = tri.pop(tri.index(max(tri)))
   if longest >= tri[0]+tri[1]:
       print('Invalid')
       continue
   else:
        tri.append(longest)
        cnt = 0
        for i in range(1, 3):
            if tri[i-1] == tri[i]:
                cnt += 1
        if cnt == 0:
            if tri[0] == tri[2]:
                print('Isosceles')
            else:
                print('Scalene')
        elif cnt == 1:
            print('Isosceles')
        elif cnt == 2:
            print('Equilateral')

