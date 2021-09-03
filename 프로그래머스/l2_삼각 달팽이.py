def solution(n):
    grid = [[0]*n for _ in range(n)]
    maxNum = sum([i for i in range(1, n+1)])
    move = [(1,0), (0,1), (-1,-1)] # DOWN -> RIGHT -> UP -> DOWN -> ...

    x,y,d = 0,0,0

    for num in range(1, maxNum+1):
        if grid[x][y] == 0:
            grid[x][y] = num
        
        dx, dy = move[d]
        nx = x + dx
        ny = y + dy

        if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
            x += dx
            y += dy
        else:
            d = (d+1)%3
            dx,dy = move[d]
            x += dx
            y += dy

    answer = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0: break
            else              : answer.append(grid[i][j])
    
    return answer    

solution(4)