import copy

game = [list(map(int, input().split())) for _ in range(4)]
d = str(input())

if d=='R':
    for i in range(4):
        for j in range(4):
            if game[i][j] ==0:
                game[i].pop(j)
                game[i].insert(0, 0)
    for i in range(4):
        for j in range(3):
            if game[i][3-j] == game[i][2-j]:
                game[i][3-j] *=2
                game[i].pop(2-j)
                game[i].insert(0, 0)

if d=='L':
    for i in range(4):
        for j in range(4):
            if game[i][j]==0:
                game[i].remove(0)
                game[i].append(0)


    for i in range(4):
        for j in range(3):
            if game[i][j] == game[i][j+1]:
                game[i][j] *=2
                game[i].pop(j+1)
                game[i].append(0)


if d=='U' or d=='D':
    game_90 = copy.deepcopy(game)
    for i in range(4):
        for j in range(4):
            game[i][j] = game_90[3-j][i]
    # print('*****각도 비틀기***')
    # print(game)
    if d=='U':
        for i in range(4):
            for j in range(4):
                if game[i][j] ==0:
                    game[i].pop(j)
                    game[i].insert(0, 0)
        for i in range(4):
            for j in range(3):
                if game[i][3-j] == game[i][2-j]:
                    game[i][3-j] *=2
                    game[i].pop(2-j)
                    game[i].insert(0, 0)
    elif d=='D':
        for i in range(4):
            for j in range(4):
                if game[i][j]==0:
                    game[i].remove(0)
                    game[i].append(0)
    
        for i in range(4):
            for j in range(3):
                if game[i][j] == game[i][j+1]:
                    game[i][j] *=2
                    game[i].pop(j+1)
                    game[i].append(0)

    # print(game)
    game_180 = copy.deepcopy(game)
    for i in range(4):
        for j in range(4):
            game[3-j][i] = game_180[i][j]
    

for i in range(4):
    for j in range(4):
        print(game[i][j], end=' ')
    print()