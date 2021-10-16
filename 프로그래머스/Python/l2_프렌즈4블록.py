import collections
def solution(m, n, board):
    grid = collections.deque([[0]*m for _ in range(n)])
    
    
    for i in range(m):
        for j in range(n):
            grid[j][i] = board[i][j]
    
    cnt = 0
    
    while True:
        check_bomb = [[0]*m for _ in range(n)]
        # BOMB
        for i in range(n-1):
            for j in range(m-1):
                now = grid[i][j]
                if now == 'X': continue
                if now == grid[i][j+1] and now == grid[i+1][j] and now ==grid[i+1][j+1]:
                    check_bomb[i][j]=1
                    check_bomb[i][j+1]=1
                    check_bomb[i+1][j]=1
                    check_bomb[i+1][j+1]=1
        sum_bomb = 0
        for i in range(n):
            sum_bomb += sum(check_bomb[i])
        if sum_bomb ==0:
            break
        cnt += sum_bomb
        # ERASE
        for i in range(n):
            for j in range(m):
                if check_bomb[i][j]==1:
                    grid[i].pop(j)
                    grid[i].insert(0, 'X')


    return cnt