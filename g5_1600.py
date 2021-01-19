#visit[x][y] --> visit[x][y][z]로 한 게 핵심
##같은 점이라도 선택이 달라질 수 있다. horse moving(k)가 더 있고 없고의 차이가 유의미하기 때문이다.
### 그래서 visit[x][y][k-1]] = visit[x][y][k] + 1 이렇게 해서 count와 visit을 함께 처리한다.



# import sys
# input = sys.stdin.readline

# import collections


# k = int(input())
# w, h = map(int, input().split())

# zoo = [list(map(int, input().split())) for _ in range(w)]
# visit = [[[0 for _ in range(31)]*w] for _ in range(h)]

# dy = [-1, 1, 0 , 0]
# dx = [0, 0, -1, 1]
# hy = [1, 2, 2, 1, -1, -2, -2, -1]
# hx = [-2, -1, 1, 2, -2, -1, 1, 2]

# results = []

# queue = collections.deque()

# # y, x, k
# queue.append((0, 0, k))
# visit[0][0] =1

# while queue:
    
#     y, x, k = queue.popleft()
#     #print(queue)
    
#     if x==h-1 and y==w-1:
#         results.append(cnt)
#         break
#     # monkey moving
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0<=ny<h and 0<=nx<w and visit[ny][nx]==0 and zoo[ny][nx]==0:
#             queue.append((ny, nx, cnt+1, k))
#             visit[ny][nx]=1
    
#     # horse moving
#     if k>0:
#         for j in range(8):
#             ny = y + hy[j]
#             nx = x + hx[j]
#             if 0<=ny<h and 0<=nx<w and visit[ny][nx]==0 and zoo[ny][nx]==0:
#                 queue.append((ny, nx, cnt+1, k-1))
#                 visit[ny][nx]=1

# if not results:
#     print(-1)
# else:
#     print(min(results))
# #print(results)


from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
d1 = [-2, -1, 1, 2, 2, 1, -1, -2]
d2 = [1, 2, 2, 1, -1, -2, -2, -1]
def bfs():
    q = deque()
    q.append((0, 0, k))
    visit = [[[0 for i in range(31)] for i in range(w)] for i in range(h)]
    while q:
        x, y, z = q.popleft()
        if x == h - 1 and y == w - 1: return visit[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != 1 and visit[nx][ny][z] == 0:
                visit[nx][ny][z] = visit[x][y][z] + 1
                q.append((nx, ny, z))
        if z > 0:
            for i in range(8):
                nx = x + d1[i]
                ny = y + d2[i]
                if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != 1 and visit[nx][ny][z - 1] == 0:
                    visit[nx][ny][z - 1] = visit[x][y][z] + 1
                    q.append((nx, ny, z - 1))
    return -1
k = int(input())
w, h = map(int, input().split())
s = [list(map(int, input().split())) for i in range(h)]
print(bfs())