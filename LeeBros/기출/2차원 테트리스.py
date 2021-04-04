import sys
import pprint
import copy
input = sys.stdin.readline

k = int(input())
block = []
for _ in range(k):
    t, x, y = map(int, input().split())
    block.append((t,x,y))

grid = [[[0 for _ in range(4)] for _ in range(6)] for _ in range(2)]




def blocking(d,t,x,y):
    x=-1
    if t==1:
        while True:
            if x==5 or grid[d][x+1][y] ==1:
                grid[d][x][y] = 1
                break
            else:
                x +=1
    elif t==2:
        while True:
            if x==5 or grid[d][x+1][y]==1 or grid[d][x+1][y+1]==1:
                grid[d][x][y]=1
                grid[d][x][y+1] =1
                break
            else:
                x+=1
    elif t==3:
        while True:
            if x==4 or grid[d][x+2][y]==1:
                grid[d][x][y]=1
                grid[d][x+1][y]=1
                break
            else:
                x+=1

def calc_score():
    global score
    for d in range(2):
        for i in range(2,6):
            combo = True
            if 0 in grid[d][i]:
                combo = False
            if combo:
                score+=1

                for x in range(i,0,-1):
                    for y in range(4):
                        grid[d][x][y] = grid[d][x-1][y]
                        grid[d][x-1][y] = 0

def eliminate_light():
    for d in range(2):
        check = 2
        for i in range(2):
            if 0 in grid[d][i]:
                check-=1

        
        if check ==2:
            new_grid = copy.deepcopy(grid[d][0:4])
            for i in range(0,2):
                for j in range(4):
                    grid[d][i][j] = 0
            grid[d][2:6] = new_grid

        elif check ==1:
            new_grid = copy.deepcopy(grid[d][1:5])
            for i in range(0,2):
                for j in range(4):
                    grid[d][i][j] = 0
            grid[d][2:6] = new_grid
        




score = 0
for t,x,y in block:
    print(t,x,y)
    print('before', grid[0])
    # yel
    blocking(0, t,x,y)
    # red
    if t ==1:
        blocking(1, 1, 0, 3-x)
    elif t==2:
        blocking(1, 3, 0, 3-x)
    elif t==3:
        blocking(1, 2, 0, 2-x)

    print(grid[0])
    calc_score()
    print(grid[0])
    eliminate_light()
    print(grid[0])


print(score)
cnt = 0
for d in range(2):
    for i in range(2,6):
        cnt += sum(grid[d][i])
print(cnt)