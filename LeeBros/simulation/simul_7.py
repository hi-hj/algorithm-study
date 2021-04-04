import copy

game = [list(map(int, input().split)()) for _ in range(4)]
d = str(input())
#d = str(input())

if d =='R':
    for i in range(4):
        for j in range(4):
            if game[i][j] == 0:
                game[i].pop(j)
                game[i].insert(0, 0)
    for i in range(4):
        for j in range(3):
            if game[i][3-j] == game[i][2-j]:
                game[i][3-j] *=2
                game[i].pop(2-j)
                game[i].insert(0, 0)

elif d=='L':
    for i in range(4):
        for j in range(4):
            if game[i][j] == 0:
                game[i].pop(j)
                game[i].append(0)

    for i in range(4):
        for j in range(3):
            if game[i][j] == game[i][j+1]:
                game[i][j] *=2
                game[i].pop(j+1)
                game[i].append(0)


#U & D 고민
elif d=='U' or d=='D':
    print(game)
    game_90 = copy.deepcopy(game)
    for i in range(4):
        for j in range(4):
            game[i][j] = game[j][i]
    print(game)

#print(game)