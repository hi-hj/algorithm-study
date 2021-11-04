class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.answer = 0
        n = len(grid)
        m = len(grid[0])
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        def bfs(x,y):
            queue = deque()
            queue.append((x,y))
            grid[x][y] = 1
            closed = True
            
            while queue:
                x, y = queue.popleft()
                if x==0 or x==n-1 or y==0 or y==m-1:
                    closed = False
                
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0:
                        grid[nx][ny] =1
                        queue.append((nx,ny))
            
            # print(closed)
            if closed:
                self.answer+=1
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    bfs(i,j)
        
        return self.answer