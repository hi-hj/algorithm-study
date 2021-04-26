import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
add_grid = [list(map(int, input().split())) for _ in range(n)]


virus = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r,c,y = map(int, input().split())
    virus[r-1][c-1].append(y)

grid = [[5]*n for _ in range(n)]
death_virus = []

# Step 1
def step_one():

    for i in range(n):
        for j in range(n):
            if virus[i][j]:
                virus[i][j].sort()
                for k in range(len(virus[i][j])):
                    year = virus[i][j][k]
                    if grid[i][j]>=year:
                        virus[i][j][k] +=1
                        grid[i][j] -= year
                    else:
                        death_virus.append((i,j,year))
    for x,y,year in death_virus:
        if year in virus[x][y]: virus[x][y].remove(year)


def step_two():
    global death_virus
    for x,y,year in death_virus:
        grid[x][y] += int(year/2)
    death_virus=[]


def step_three():
    
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    for x in range(n):
        for y in range(n):
            if virus[x][y]:
                for k in range(len(virus[x][y])):
                    year = virus[x][y][k]
                    if year %5 ==0:
                        for d in range(8):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if 0<=nx<n and 0<=ny<n:
                                virus[nx][ny].append(1)


def step_four():
    for i in range(n):
        for j in range(n):
            grid[i][j] += add_grid[i][j]


for i in range(k):
    step_one()
    step_two()
    step_three()
    step_four()


answer = 0
for i in range(n):
    for j in range(n):
        if virus[i][j]:
            for k in range(len(virus[i][j])):
                answer +=1
print(answer)
# print(len(virus))