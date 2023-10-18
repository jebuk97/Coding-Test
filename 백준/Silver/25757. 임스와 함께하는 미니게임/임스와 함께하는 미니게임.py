n, game = input().split()
players = [input() for _ in range(int(n))]

#Y 2, F 3, O 4
players = set(players)
if game == 'Y':
    print(len(players))
elif game == 'F':
    print(len(players)//2)
elif game == 'O':
    print(len(players)//3)