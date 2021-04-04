import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

r,c,m1,m2,_,_,d = map(int, input().split())
r,c = r-1,c-1


def rotate(x,y,m1,m2,d):
    array = []
    # 1
    for i in range(m1):
        array.append((x-i, y+i, grid[x-i][y+i]))
    # 2
    for j in range(m2):
        array.append((x-m1-j, y+m1-j, grid[x-m1-j][y+m1-j]))
    # 3
    for i in range(m1):
        array.append((x-m1-m2+i, y+m1-m2-i, grid[x-m1-m2+i][y+m1-m2-i]))
    # 4
    for j in range(m2):
        array.append((x-m2+j, y-m2+j, grid[x-m2+j][y-m2+j]))

    if d==0:
        _, _, lv = array[-1]
        fx, fy, _ = array[0]
        for i in range(2*(m1+m2)):
            if i == 2*(m1+m2)-1:
                break

            _, _, v = array[i]
            nx, ny, _ = array[i+1]
            grid[nx][ny] = v
        grid[fx][fy] = lv
    
    elif d==1:
        _, _, fv = array[0]
        lx, ly, _ = array[-1]
        for i in range(1, 2*(m1+m2)):
            _, _, v = array[i]
            bx, by, _ = array[i-1]
            grid[bx][by] = v
        grid[lx][ly] = fv
    

rotate(r,c,m1,m2,d)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()
