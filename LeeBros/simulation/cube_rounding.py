import sys

n, m, x, y, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
direc = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
cube=[0]*6



def move_cube(cube, direc):
    if direc ==1:
        cube[3], cube[5], cube[2], cube[0] = cube[0], cube[3], cube[5], cube[2]
    elif direc == 2:
        cube[2], cube[5], cube[3], cube[0] = cube[0], cube[2], cube[5], cube[3]
    elif direc == 3:
        cube[4], cube[5], cube[1], cube[0] = cube[0], cube[4], cube[5], cube[1]
    elif direc == 4:
        cube[1], cube[5], cube[4], cube[0] = cube[0], cube[1], cube[5], cube[4]
    return cube

for d in direc:    
    nx = x +dx[d]
    ny = y +dy[d]
    if 0<=nx<n and 0<=ny<m:
        x, y = nx, ny
        cube = move_cube(cube, d)

        if grid[x][y] == 0:
            grid[x][y] = cube[0]
        else:
            cube[0] = grid[x][y]
            grid[x][y] = 0
        
        print(cube[5])