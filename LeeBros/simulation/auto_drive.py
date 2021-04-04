import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]

cnt = 0
move = 0
grid[x][y] = 2

while True:
    # 좌측 nx , ny
    nx = x + dx[(d-1)%4]
    ny = y + dy[(d-1)%4]
    # Step 1: 좌측 갈 수 있으면 감
    if grid[nx][ny]==0:
        grid[nx][ny] = 2
        d = (d-1)%4
        x, y = nx, ny
        cnt = 0
        continue
    
    # Step 3
    if cnt == 4:
        bx = x + dx[(d+2)%4]
        by = y + dy[(d+2)%4]
        if grid[bx][by]!=1:
            grid[bx][by] = 2
            x, y = bx, by
            cnt = 0
            continue
        else:
            break
    
    # Step 2: 좌측 못 감
    elif cnt!=4 and grid[nx][ny]!=0:
        d = (d-1)%4
        cnt +=1
        continue


answer = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            answer +=1

print(answer)
    