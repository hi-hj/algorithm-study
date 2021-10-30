import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
      
        if not heightMap:
            return 0
        
        n = len(heightMap)
        m = len(heightMap[0])
        
        h = []
        grid = [[0]*m for _ in range(n)]
        re = 0
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n-1 or j == m-1:
                    grid[i][j] = 1
                    heapq.heappush(h, (heightMap[i][j], i, j))
        

        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        
        while h:
            curh, x, y = heapq.heappop(h)
            print(curh, x,y)

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or ny < 0 or nx >= n or ny>= m:
                    continue
                if grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    
                    if curh > heightMap[nx][ny]:
                        print(curh, heightMap[nx][ny], " - X/Y", x,y, " - NX/NY", nx,ny)
                        re += (curh - heightMap[nx][ny])
                        heapq.heappush(h, (curh, nx, ny))
                    else:
                        heapq.heappush(h, (heightMap[nx][ny], nx, ny))
        
        return re

Solution().trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]])
# Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])