import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(str, input())) for _ in range(n)]
c = [[0]*m for _ in range(n)]
q, wq = deque(), deque()

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def water():
    qlen = len(wq)
    while qlen:
        x, y = wq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if a[nx][ny]=='.':
                    a[nx][ny]='*'
                    wq.append([nx,ny])
        qlen -=1
def bfs(x, y):
    q.append([x,y])
    c[x][y]=1
    
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if a[nx][ny]=='.' and c[nx][ny]==0:
                        c[nx][ny]=c[x][y]+1
                        q.append([nx,ny])
                    elif a[nx][ny]=='D':
                        print(c[x][y])
                        return
            qlen -=1
        water()
    print('KAKTUS')
    return

for i in range(n):
    for j in range(m):
        if a[i][j] =='S':
            x1, y1 = i, j
            a[i][j] = '.'
        elif a[i][j] =='*':
            wq.append([i, j])

water()
bfs(x1, y1)
# # INPUT &  SETTING
# r, c = map(int, input().split())
# forest = []
# water = []
# dy = [0, 0, -1, 1]
# dx = [-1, 1, 0 , 0]

# for i in range(r):
#     row = list(input().strip())
#     for j in range(len(row)):
#         if row[j]=='D':
#             dl = (i, j)
#         elif row[j]=='S':
#             sl = (i, j)
#     forest.append(row)
#     water.append(row)

# sibal = True
# for i in range(r):
#     for j in range(c):
#         if water[i][j]=='S':
#             water[i][j]='.'
#         if water[i][j]=='*':
#             sibal = False
 
# def move_water():
#     global water
#     w_list = []
#     for i in range(r):
#         for j in range(c):
#             if water[i][j]=='*':
#                 w_list.append((i, j))
    
#     while w_list:
#         wi, wj = w_list.pop()
#         for k in range(4):
#             ny = wi + dy[k]
#             nx = wj + dx[k]
#             if 0<=ny<r and 0<=nx<c:
#                 if water[ny][nx]=='.' or water[ny][nx]=='S':
#                     water[ny][nx]='*'

# def bfs():
#     queue = collections.deque()
#     queue.append((sl,0))
#     #print(sl)
#     results = []
#     visit = [[[0 for _ in range(50)] for _ in range(c)] for _ in range(r)]

#     while queue:
#         s, cnt = queue.popleft()
#        # print(s, cnt)
#         move_water()

#         if forest[s[0]][s[1]]=='D':
#             return visit[s[0]][s[1]][cnt]
        
#         for i in range(4):
#             ny = s[0]+dy[i]
#             nx = s[1]+dx[i]
#             new_s = (ny, nx)
  
#             if 0<=ny<r and 0<=nx<c:
#               #  print(forest[ny][nx])
#                 if forest[ny][nx]=='D':
#                     queue.append((new_s, cnt+1))
#                     visit[ny][nx][cnt+1] = visit[s[0]][s[1]][cnt] + 1
#                 elif forest[ny][nx]!='X' and water[ny][nx]!='*' and visit[ny][nx][cnt]==0 and cnt+1<100:
#                     #print(new_s)
#                     queue.append((new_s, cnt+1))
#                     visit[ny][nx][cnt+1] = visit[s[0]][s[1]][cnt] + 1
#                 #print(visit[ny][nx][cnt+1])
# if sibal:
#     print(r+c-2)
# else:
#     a = bfs()
#     if a:
#         print(a)
#     else:
#         print('KAKTUS')



        
        

