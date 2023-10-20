T = int(input())

for _ in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    team = [[] for _ in range(201)]
    teams = set()
    for i, d in enumerate(data):
        if len(team[d]) == 0:
            teams.add(d)
        team[d].append(i+1)
    minTeam = []
    minPoint = 9999999
    removes = []
    for t in teams:
        if len(team[t]) < 6:
            removes.append(t)
    for r in removes:
        teams.remove(r)
    team = [[] for _ in range(201)]
    idx = 1
    for i, d in enumerate(data):
        if d in teams:
            team[d].append(idx)
            idx += 1

    minPoint = 999999
    minTeam = []
    for t in teams:
        p = sum(team[t][:4])
        if p < minPoint:
            minPoint = p
            minTeam = [t]
        elif p == minPoint:
            minTeam.append(t)
    # print(minTeam)
    if len(minTeam) > 1:
        minPoint = 999999
        for m in minTeam:
            # print(team[m])
            if team[m][4] < minPoint:
                minPoint = team[m][4]
                minTeam = [m]

    print(minTeam[0])