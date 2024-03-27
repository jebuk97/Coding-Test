def solution(numbers, hand):
    answer = ''
    lefthand = 10
    righthand = 12
    for n in numbers:
        if n == 0:
            n = 11
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            lefthand = n
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            righthand = n
        else:
            ldist = abs(((n-1) // 3) - ((lefthand-1) // 3)) + abs((lefthand-1)%3 -(n-1)%3)
            rdist = abs(((n-1) // 3) - ((righthand-1) // 3)) + abs((righthand-1)%3 -(n-1)%3)
            if ldist > rdist:
                answer += 'R'
                righthand = n
            elif ldist < rdist:
                answer += 'L'
                lefthand = n
            else:
                if hand == 'left':
                    answer += 'L'
                    lefthand = n
                else:
                    answer += 'R'
                    righthand = n
            
    return answer