import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


chess = []
others = []
for i in range(n):
    for j in range(m):
        if grid[i][j]!=0 and grid[i][j]!=6:
            chess.append([grid[i][j], 0, (i, j)])
        elif grid[i][j] == 6:
            others.append((i, j))





dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def calc_area(now_chess):
    can_go = [[False]*m for _ in range(n)]

    for num, vec, (x, y) in now_chess:
        
        if num ==1:
            for i in range(1, 8):
                nx = x + dx[vec]*i
                ny = y + dy[vec]*i
                if 0<=nx<n and 0<=ny<m:
                    if (nx, ny) in others: break
                    can_go[nx][ny] = True
                else: break

        elif num==2:
            for i in range(2):

                for i in range(1, 8):
                    nx = x + dx[vec]*i
                    ny = y + dy[vec]*i
                    if 0<=nx<n and 0<=ny<m:
                        if (nx, ny) in others: break
                        can_go[nx][ny] = True

                    else: break

                vec = (vec+2)%4
                

        elif num==3:
            for i in range(2):
                for i in range(1, 8):
                    nx = x + dx[vec]*i
                    ny = y + dy[vec]*i
                    if 0<=nx<n and 0<=ny<m:
                        if (nx, ny) in others: break
                        can_go[nx][ny] = True
                    else: break
                vec = (vec+1)%4

              
        elif num==4:
            for i in range(3):
                for i in range(1, 8):
                    nx = x + dx[vec]*i
                    ny = y + dy[vec]*i
                    if 0<=nx<n and 0<=ny<m:
                        if (nx, ny) in others: break
                        can_go[nx][ny] = True
                    else: break
                vec = (vec+1)%4
        
        

        elif num==5:

            for i in range(4):
                i =1
                while i<8:

                    nx = x + dx[vec]*i
                    ny = y + dy[vec]*i

                    if 0<=nx<n and 0<=ny<m:
                        if (nx, ny) in others: break
                        can_go[nx][ny] = True
                    else: break
                    i +=1
                vec = (vec+1)%4
    
    for num, vec, (x, y) in now_chess:
        can_go[x][y] = True
    for x,y in others:
        can_go[x][y] = True

    result = 0
    for i in range(n):
        for j in range(m):
            if can_go[i][j] == False:
                result +=1
    return result


answer = sys.maxsize

def dfs(cur_idx, cur_list):
    global answer
    if cur_idx == len(chess):
        answer = min(answer, calc_area(cur_list))
        return
    
    for i in range(4):
        cur_list[cur_idx][1] = i
        dfs(cur_idx+1, cur_list)

dfs(0, chess)

print(answer)



