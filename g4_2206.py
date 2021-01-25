import sys
import collections
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


n, m = map(int, input().split())
wmap = [list(map(int, input().strip())) for _ in range(n)]
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]


def bfs():
    queue = collections.deque()
    queue.append((0, 0, 1))
    visit[0][0][0] = 1
    while queue:
        y, x, chance = queue.popleft()
        if y==n-1 and x==m-1:
            return visit[y][x][chance]+1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                # 벽 있는 경우
                if wmap[ny][nx]==1 and chance==1:
                    visit[ny][nx][0] = visit[y][x][chance] + 1
                    queue.append((ny, nx, 0))
                elif wmap[ny][nx]==0 and visit[ny][nx][chance]==0:
                    visit[ny][nx][chance] = visit[y][x][chance] +1
                    queue.append((ny, nx, chance))
    return -1

print(bfs())



# def bfs():
#     q = deque()
#     q.append((0,0,1))
#     visit = [[[0]*2 for i in range(m)] for _ in range(n)]
#     visit[0][0][0] =1

#     while q:
#         a, b, w = q.popleft()
#         if a==n-1 and b==m-1:
#             return visit[a][b][w]
        
#         for i in range(4):
#             x = a+dx[i]
#             y = b+dy[i]
#             if 0<=x<n and 0<=y<m:
#                 # 벽 인경우 + 찬스가 있는경우
#                 # 방문 체크? 어차피 한 번이라서..
#                 if s[x][y]==1 and w==1:
#                     visit[x][y][0] = visit[a][b][1]+1
#                     q.append([x,y,0])

#                 # 벽이 아닌 경우, 방문을 안 한 경우    
#                 elif s[x][y]==0 and visit[x][y][w]==0:
#                     visit[x][y][w] = visit[a][b][w]+1
#                     q.append([x,y,w])
#         return -1
# n, m = map(int, input().split())
# s= []
# for i in range(n):
#     s.append(list(map(int, list(input().strip())))

# print(bfs())

# import sys
# input = sys.stdin.readline

# import collections

# n, m = map(int, input().split())
# wmap = [list(map(int, input().strip())) for _ in range(n)]
# visit = [[0]*m for _ in range(n)]

# dy = [-1,1,0,0]
# dx = [0,0,-1,1]
# results = []
# def bfs(y, x, cnt):
#     queue = collections.deque()
#     queue.append((y, x, cnt))
#     visit[y][x] = 1
#     chance = 1

#     while queue:
#         y, x, cnt = queue.popleft()
#         if y==n-1 and x==m-1:
#             results.append(cnt)
#             return
        
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0<=ny<n and 0<=nx<m and visit[ny][nx]==0:
#                 # 벽 없는 4개
#                 if wmap[ny][nx]==0:
#                     visit[ny][nx]=1
#                     queue.append((ny, nx, cnt+1))
#         if chance==1:
#             for i in range(4):
#                 ny = y+dy[i]
#                 nx = x+dx[i]
#                 if 0<=ny<n and 0<=nx<m and visit[ny][nx]==0 and wmap[ny][nx]==1:
#                     visit[ny][nx]=1
#                     chance=0
#                     queue.append((ny, nx, cnt+1))
#     return -1
# a = bfs(0,0,1)

# if a:
#     print(a)
# else:
#     print(min(results))
