import sys
import copy
import math
input = sys.stdin.readline

n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



wind = []
for i in range(n):
    if grid[i][0] == -1:
        wind.append(i)
# print(wind)

for _ in range(t):
    new_grid = [[0]*m for _ in range(n)]
    # DUST MOVE
    for x in range(n):
        for y in range(m):
            if grid[x][y] == -1:
                new_grid[x][y]=-1
                continue
            div = math.floor(grid[x][y]/5)
            cnt = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]!=-1:
                    new_grid[nx][ny] += div
                    cnt +=1
            new_grid[x][y] += grid[x][y] - cnt*div

    grid = new_grid
    # print(grid)

    # UPPER WIND (n, 0)
    up = wind[0]
    new_grid = copy.deepcopy(grid)
    for y in range(0, m-1, 1):
        grid[up][y+1] = new_grid[up][y]
    for x in range(up, 0, -1):
        grid[x-1][m-1] = new_grid[x][m-1]
    for y in range(m-1, 0, -1):
        grid[0][y-1] = new_grid[0][y]
    for x in range(0, up, 1):
        grid[x+1][0] = new_grid[x][0]

    grid[up][0] = -1
    grid[up][1] = 0

    # DOWN WIND
    down = wind[1]
    for y in range(0, m-1, 1):
        grid[down][y+1] = new_grid[down][y]
    for x in range(down, n-1, 1):
        grid[x+1][m-1] = new_grid[x][m-1]
    for y in range(m-1, 0, -1):
        grid[n-1][y-1] = new_grid[n-1][y]
    for x in range(n-1, down, -1):
        grid[x-1][0] = new_grid[x][0]

    grid[down][0] = -1
    grid[down][1] = 0

# print(grid)

answer = 0
for i in range(n):
    for j in range(m):
        answer += grid[i][j]
answer +=2
print(answer)