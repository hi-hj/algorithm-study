import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())

grid = [list(input().strip()) for _ in range(n)]


for i in range(n):
    for j in range(m):
        if grid[i][j] == 'R': red = (i, j)
        elif grid[i][j] == 'B': blue = (i, j)
        elif grid[i][j] == 'O': out = (i, j)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def red_first(direc):
    rx, ry = red
    bx, by = blue

    if direc == 0:
        return (ry==by and rx<bx)
    elif direc==1:
        return (ry==by and rx>bx)
    elif direc==2:
        return (rx==bx and ry<by)
    elif direc==3:
        return (rx==bx and ry>by)

def can_go(x, y):
    return grid[x][y]!='#' and (x, y) != red and (x, y) !=blue


def get_detination(pos, move_dir):
    cur_x, cur_y = pos
    nx, ny = cur_x + dx[move_dir], cur_y + dy[move_dir]

    if not can_go(nx, ny):
        return pos
    if grid[nx][ny] == out:
        return (n, m)
    


