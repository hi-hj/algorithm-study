import sys
import copy
input = sys.stdin.readline

input_grid = [list(map(int, input().split())) for _ in range(4)]
grid = [[(0,0)]*4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        grid[i][j] = [input_grid[i][2*j], input_grid[i][2*j+1]-1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def move_thieve():
    can_go = []
    for i in range(4):
        for j in range(4):

            can_go.append((grid[i][j][0], False))
    can_go.sort()

    for num, visited in can_go:
        if num == 0 or num == 1004: continue
        for x in range(4):
            for y in range(4):
                if grid[x][y][0] == num and visited==False:
                    cnt = 0
                    while cnt < 8:
                        d = grid[x][y][1]
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0<=nx<4 and 0<=ny<4 and grid[nx][ny][0]!=1004:
                            grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
                            break
                        else:
                            grid[x][y][1] = (d+1)%8
                            cnt +=1
                    visited = True
    return grid


def move_horse(hx, hy, score, grid):
    global answer
    hd = grid[hx][hy][1]
    can_go = []
    for i in range(1,5):
        nx = hx + dx[hd]*i
        ny = hy + dy[hd]*i
        if 0<=nx<4 and 0<=ny<4 and grid[nx][ny][0]!=0:
            temp_grid = [[grid[i][j] for j in range(4)] for i in range(4)]
            extra_score= grid[nx][ny][0]
            grid[nx][ny][0], grid[hx][hy][0] = 1004, 0
            grid = move_thieve(grid)
            move_horse(nx, ny, score, grid)
            for i in range(4):
                for j in range(4):
                    grid[i][j] = temp_grid[i][j]
    if not can_go:
        print(score)
        print(grid)
        answer = max(answer, score)
        return

answer = 0

score = 0
score += grid[0][0][0]
grid[0][0][0] = 1004

move_horse(0, 0, score, grid)
print(answer)