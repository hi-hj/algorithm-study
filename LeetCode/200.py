from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        
        n = len(grid)
        m = len(grid[0])
        
        
        def bfs(x:int, y:int):
            queue = deque()
            queue.append((x,y))
            grid[x][y] = "0"
            
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            
            while queue:
                x,y = queue.popleft()
                
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]=="1":
                        queue.append((nx,ny))
                        grid[nx][ny] = "0"
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    island+=1
                    bfs(i,j)
        
        return island