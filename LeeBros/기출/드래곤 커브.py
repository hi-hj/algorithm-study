import sys
import collections
input = sys.stdin.readline

n = int(input())
dragon = [list(map(int, (input().split()))) for _ in range(n)]

grid = [[0]*100 for _ in range(100)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def rotate(x, y, cx, cy):
    return (y-cy+cx, cx-x+cy)


def make_dragon(x, y, d, g):
    global grid
    dragon = []
    
    dragon.append((x, y))
    # 0차시 세팅
    x = x + dx[d]
    y = y + dy[d]
    dragon.append((x, y))
    sx, sy = dragon[0]

    for i in range(g):
        new_dragon = []
        cx, cy = dragon[-1]
        for j in range(1, len(dragon)):
            x,y = dragon[j]
            new_dragon.append(rotate(x,y,cx,cy))
        new_dragon.append(rotate(sx,sy, cx, cy))
        dragon += new_dragon
    for x,y in dragon:
        grid[x][y] = 1

for x,y,d,g in dragon:
    make_dragon(x,y,d,g)

answer = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] ==1 and grid[i][j+1]==1 and grid[i+1][j]==1 and grid[i+1][j+1]==1:
            answer +=1

print(answer)
    
    
