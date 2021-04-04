import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

square = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]


eng = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

cnt = 0


def dfs(x, y, cnt, direc):
    visit[x][y] = 1
    square[x][y] = eng[cnt]
    cnt +=1
    if cnt >= 26:
        cnt -= 26

    if direc==1:
        if y+1 < m and visit[x][y+1]==0:
            dfs(x, y+1, cnt, 1)
    elif direc==2:
        if x+1 < n and visit[x+1][y]==0:
            dfs(x+1, y, cnt, 2)
    elif direc==3:
        if 0<= y-1 and visit[x][y-1]==0:
            dfs(x, y-1, cnt, 3) 
    elif direc==4:
        if 0<= x-1 and visit[x-1][y]==0:
            dfs(x-1, y, cnt, 4)

    if y+1 < m and visit[x][y+1]==0:
        dfs(x, y+1, cnt, 1)
    elif x+1 < n and visit[x+1][y]==0:
        dfs(x+1, y, cnt, 2)
    elif 0<= y-1 and visit[x][y-1]==0:
        dfs(x, y-1, cnt, 3) 
    elif 0<= x-1 and visit[x-1][y]==0:
        dfs(x-1, y, cnt, 4)


dfs(0, 0, 0, 1)

for i in range(n):
    for j in range(m):
        print(square[i][j], end =' ')
    print()
#print(square)
