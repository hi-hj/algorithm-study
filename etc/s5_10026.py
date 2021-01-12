from collections import deque

N = int(input())
arr = [list(input().strip()) for _ in range(N)]

NormalVisited = [[0]*N for _ in range(N)]
NormalCnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

#정상인
for i in range(N):
    for j in range(N):
        if NormalVisited[i][j]==0:
            NormalCnt +=1
            q.append([i,j])
            NormalVisited[i][j] = 1
            now = arr[i][j]

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<N and 0<=ny<N and NormalVisited[nx][ny]==0 and arr[nx][ny]==now:
                        q.append([nx, ny])
                        NormalVisited[nx][ny] = 1


Inarr = arr
for i in range(N):
    for j in range(N):
        if Inarr[i][j]=='G':
            Inarr[i][j]='R'
InnomralVistied = [[0]*N for _ in range(N)]
InnomralCnt = 0


#적녹색맹
for i in range(N):
    for j in range(N):
        if InnomralVistied[i][j]==0:
            InnomralCnt +=1
            q.append([i,j])
            InnomralVistied[i][j] = 1
            now = Inarr[i][j]
            
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<N and 0<=ny<N and InnomralVistied[nx][ny]==0 and Inarr[nx][ny]==now:
                        q.append([nx, ny])
                        InnomralVistied[nx][ny] = 1

print(NormalCnt, InnomralCnt)

            
    