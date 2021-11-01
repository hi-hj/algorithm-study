class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visited = set()
        n = len(grid)
        m = len(grid[0])
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        queue = deque()
        queue.append((0, (0,0,k))) # step / (x,y,k)
        visited.add((0,0,k))
        
        while queue:
            step, (x,y,k) = queue.popleft()
            
            if x==n-1 and y==m-1:
                return step
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<n and 0<=ny<m:
                    nk = k - grid[nx][ny]
                    if nk>=0 and (nx,ny,nk) not in visited:
                        visited.add((nx,ny,nk))
                        queue.append((step+1, (nx,ny,nk)))
        
        return -1