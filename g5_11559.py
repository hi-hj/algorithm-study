import sys
input = sys.stdin.readline
import collections










































# graph = [list(input().strip()) for _ in range(12)]
# puyo = [[0]*12 for _ in range(6)]

# for i in range(12):
#     for j in range(6):
#         puyo[j][11-i] = graph[i][j]

# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]

# cnt = 0

# def bfs(sc, y, x):
#     queue = collections.deque()
#     queue.append((y,x))
#     visit[y][x]=1
#     results = [(y, x)]

#     while queue:
#         y, x = queue.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0<=ny<6 and 0<=nx<12 and visit[ny][nx]==0 and puyo[ny][nx]==sc:
#                 visit[ny][nx]=1
#                 results.append((ny, nx))
#                 queue.append((ny, nx))

#     if len(results)>=4:
#         for y, x in results:
#             umm.append((y, x))
#         global no_more
#         no_more = False


# no_more = False
# while not no_more:
#     no_more = True
#     # One circle
#     visit = [[0]*12 for _ in range(6)]
#     umm = []


#     for i in range(6):
#         for j in range(12):
#             if visit[i][j]==0 and puyo[i][j]!='.':
#                 bfs(puyo[i][j], i, j)


#     #print(umm)
#     if umm:
#         cnt+=1
#         for y, x in umm:
#             puyo[y][x]=0

#     # Reset
#     for i in range(6):
#         j=0
#         while j<12:
#             if puyo[i][j]==0:
#                 puyo[i] = puyo[i][1:]+['.']
#                 j-=1
#             j+=1

# while not no_more:
#     no_more = True


#     # One circle
#     visit = [[0]*12 for _ in range(6)]
#     umm = []



#     for i in range(6):
#         for j in range(12):
#             if visit[i][j]==0 and puyo[i][j]!='.':
#                 bfs(puyo[i][j], i, j)
#     print(umm)
#     # Reset
#     for i in range(6):
#         j=0
#         while j<12:
#             if puyo[i][j]==0:
#                 puyo[i] = puyo[i][1:]+['.']
#                 j-=1
#             j+=1

print(cnt)
