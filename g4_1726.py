import sys
input = sys.stdin.readline
import collections

m, n = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(m)]

def minus(a):
    a = int(a)
    return a-1

x1, y1, d1 = map(minus, input().split())
x2, y2, d2 = map(minus, input().split())

dx = [0, 0, 0, 0, 0, 0, 1, 2, 3, -1, -2, -3]
dy = [1, 2, 3, -1, -2, -3, 0, 0, 0, 0 ,0 ,0]

direct = {0:[2, 3], 1:[2, 3], 2:[0,1], 3:[0,1]}
# for i in direct[0]:
#     print(i)

    
def bfs(x1, y1, d1):
    queue = collections.deque()
    queue.append((x1, y1, d1))
    visited[x1][y1][d1] = -1

    while queue:
        x, y, d = queue.popleft()
        #print(x, y, d, visited[x][y][d])

        if x==x2 and y==y2 and d==d2:
            return visited[x2][y2][d2]
        # 터닝
        for nd in direct[d]:
            if visited[x][y][nd]==0:
                visited[x][y][nd] = visited[x][y][d] -1
                queue.append((x, y, nd))

        # 직진
        if d==0:
            for i in range(0, 3):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n:
                    if factory[nx][ny]==1: break
                    elif factory[nx][ny]==0 and visited[nx][ny][d]==0:
                        visited[nx][ny][d] = visited[x][y][d] -1
                        queue.append((nx, ny, d))
       
        if d==1:
            for i in range(3, 6):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n:
                    if factory[nx][ny]==1: break
                    elif factory[nx][ny]==0 and visited[nx][ny][d]==0:
                        visited[nx][ny][d] = visited[x][y][d] -1
                        queue.append((nx, ny, d))
               
        if d==2:
            for i in range(6, 9):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n:
                    if factory[nx][ny]==1: break
                    elif factory[nx][ny]==0 and visited[nx][ny][d]==0:
                        visited[nx][ny][d] = visited[x][y][d] -1
                        queue.append((nx, ny, d))
    
        if d==3:
            for i in range(9, 12):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n:
                    if factory[nx][ny]==1: break
                    elif factory[nx][ny]==0 and visited[nx][ny][d]==0:
                        visited[nx][ny][d] = visited[x][y][d] -1
                        queue.append((nx, ny, d))
 
        


visited =[[[0]*4 for _ in range(n)] for _ in range(m)]
answer = bfs(x1, y1, d1)

print(-(answer+1))

