# 늑대와 양
import sys

R, C = map(int, sys.stdin.readline().split())
pasture = [list(sys.stdin.readline().strip()) for _ in range(R)]

#print(pasture)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = True

for i in range(R):
    for j in range(C):
        if pasture[i][j] == 'W':
            for move in range(4):
                ni, nj = i+dx[move], j+dy[move]
                if ni <0 or nj < 0 or ni==R or nj ==C:
                    continue
                elif pasture[ni][nj] =='S':
                    flag = False
        elif pasture[i][j] =='S':
            continue
        else:
            pasture[i][j] ='D'
    

if flag:
    print('1')
    for i in pasture:
        print(''.join(i))

else:
    print('0')