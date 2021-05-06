# BFS
from collections import deque

def bfs(x,y,d,c):
    queue = deque()
    queue.append((x,y,d,c)) # x,y,d,c
    visited = [[False]*n for _ in range(n)]
    visited[0][0] = True
    cost = [[0]*n for _ in range(n)]

    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    
    while queue:
        x,y,d,c = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nc = c + 100
            if (d+i)%2 ==1:
                nc +=500
            # print(x,y, nx,ny)
            
            if 0<=nx<n and 0<=ny<n and board[nx][ny]==0:
                if visited[nx][ny]==False or cost[nx][ny] > nc:
                    visited[nx][ny] = True
                    cost[nx][ny] = nc
                    queue.append((nx,ny,i,nc))
    return cost[-1][-1]

def solution(b):
    global n
    global board
    board = b
    n = len(board)
    return min(bfs(0,0,0,0), bfs(0,0,1,0))


# DFS 풀이 : 시간 초과
# import sys
# def dfs(x,y,move,cost, grid):
#     global answer
#     dx = [0,-1,0,1]
#     dy = [1,0,-1,0]
#     if (x,y)==(n-1,n-1):
#         answer = min(answer, cost)
#         return

#     if cost >= answer:
#         return
    
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         nc = cost + 100

#         if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
#             if (move + d)%2 ==1: # 직각
#                 nc+=500
#             grid[nx][ny]=2
#             dfs(nx,ny,d,nc,grid)
#             grid[nx][ny] = 0
                
# def solution(board):
#     global n
#     global answer
#     n = len(board)
#     answer = sys.maxsize

#     board[0][0] = 2
#     dfs(0,0,0,0,board)
#     dfs(0,0,1,0,board)
#     # print(answer)
#     return answer
    
    

solution([[0,0,0],[0,0,0],[0,0,0]])
#solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
#solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
#solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])