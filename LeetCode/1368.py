import sys
from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cost = [[sys.maxsize]*m for _ in range(n)]
        cost[0][0] = 0
        
        queue = deque()
        queue.append((0,0,0)) # X,Y,C
        move = {1:(0,1), 2:(0,-1), 3:(1,0), 4:(-1,0)}
        
        while queue:
            x,y,c = queue.popleft()            
            
            
            for d in move.keys():
                nx = x + move[d][0]
                ny = y + move[d][1]
                
                if 0<=nx<n and 0<=ny<m:
                    if d==grid[x][y]:
                        if c < cost[nx][ny]:
                            queue.append((nx,ny,c))
                            cost[nx][ny] = c
                    else:
                        if c+1 < cost[nx][ny]:
                            queue.append((nx,ny,c+1))
                            cost[nx][ny] = c+1
        
        return cost[-1][-1]