import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
atom = []

for _ in range(m):
    x,y,m,s,d = map(int, input().split())
    atom.append((x-1,y-1,m,s,d))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]


def move_atom(x,y,m,s,d):
    nx = (x + dx[d]*s)%n
    ny = (y + dy[d]*s)%n
    grid[nx][ny].append((m,s,d))





for _ in range(k):
    grid = [[[] for _ in range(n)] for _ in range(n)]
    for x,y,m,s,d in atom:
        move_atom(x,y,m,s,d)
    
    new_atom = []
    for x in range(n):
        for y in range(n):
            if grid[x][y] and len(grid[x][y])==1:
                for m,s,d in grid[x][y]:
                    new_atom.append((x,y,m,s,d))
            
            if grid[x][y] and len(grid[x][y])>1:
                new_m = 0
                new_s = 0
                dir_match = []
                for m,s,d in grid[x][y]:
                    new_m += m
                    new_s += s
                    dir_match.append(d%2)
                new_m = int(new_m / 5)
                new_s = int(new_s / len(grid[x][y]))
                dir_match = set(dir_match)
                if new_m > 0:
                    # 정방향
                    if len(dir_match)==1:
                        for i in range(4):
                            new_atom.append((x,y,new_m,new_s, i*2))
                    # 대각선 방향
                    elif len(dir_match)==2:
                        for i in range(4):
                            new_atom.append((x,y,new_m,new_s, i*2+1))
    atom = new_atom


answer = 0
for _,_,m,_,_ in atom:
    answer += m
print(answer)
