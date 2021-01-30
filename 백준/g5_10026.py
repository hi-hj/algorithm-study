# import sys
# input = sys.stdin.readline
# import copy
# from collections import deque

# n = int(input())
# pic = [list(input().rstrip()) for _ in range(n)]
# visited = [[0]*n for _ in range(n)]
# u_visited = copy.deepcopy(visited)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# normal_count = 0
# unnormal_count = 0
# queue = deque()

# def bfs(normal, color, x, y):
#     queue.append([x,y])
#     if normal ==0:
#         visited[x][y] = 1
#         global normal_count
#         normal_count +=1
#     else:
#         u_visited[x][y]=1
#         global unnormal_count
#         unnormal_count +=1
    
#     while queue:
#         vx, vy = queue.popleft()
#         for i in range(4):
#             nx = vx + dx[i]
#             ny = vy + dy[i]
#             if normal==0:
#                 if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
#                     if color == pic[nx][ny]:
#                         queue.append([nx, ny])
#                         visited[nx][ny] = 1
#             else:
#                 if 0<=nx<n and 0<=ny<n and u_visited[nx][ny]==0:
#                     if (color == 'R' or color=='G') and (pic[nx][ny]=='R' or pic[nx][ny]=='G'):
#                         queue.append([nx, ny])
#                         u_visited[nx][ny] = 1
#                     elif color == pic[nx][ny]:
#                         queue.append([nx, ny])
#                         u_visited[nx][ny] = 1

# for i in range(n):
#     for j in range(n):
#         if visited[i][j]==0:
#             bfs(0, pic[i][j], i, j)
#         elif u_visited[i][j]==0:
#             bfs(1, pic[i][j], i, j)

# print(normal_count, unnormal_count)


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
