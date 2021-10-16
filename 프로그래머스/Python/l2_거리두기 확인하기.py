import pprint
from collections import deque


def bfs(x,y,grid):
    queue = deque()
    queue.append((x,y,0)) # X, Y, COUNT
    visited = set()
    visited.add((x,y))
    start = (x,y)

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while queue:
        x,y,cnt = queue.popleft()
        if (x,y)!=start and grid[x][y]=='P':
            return True
        # print(x,y,cnt)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<5 and 0<=ny<5 and cnt<2:
                if grid[nx][ny]!='X' and (nx,ny) not in visited:
                    queue.append((nx,ny, cnt+1))
                    visited.add((nx, ny))
    return False
    
        

def solution(places):
    answer = []
    
    
    pprint.pprint(places)

    for place in places:
        check = False
        pprint.pprint(place)
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P':
                    check = bfs(i,j,place)
                    print(i,j, check)
                if check: break
            if check: break
        if check: answer.append(0)
        else: answer.append(1)
    
    print(answer)
        

    bfs(0,0,places[0])


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])