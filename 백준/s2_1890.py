import sys
input = sys.stdin.readline

n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
cnt_grid = [[0]*n for _ in range(n)]

cnt_grid[0][0] = 1

# Sol 2 : DP
for x in range(n):
    for y in range(n):
        if grid[x][y]!=0 and cnt_grid[x][y]!=0:
            # 오른쪽
            if y + grid[x][y] < n:
                cnt_grid[x][y + grid[x][y]] += cnt_grid[x][y]
            # 아래
            if x + grid[x][y] < n:
                cnt_grid[x + grid[x][y]][y] += cnt_grid[x][y]

print(cnt_grid[n-1][n-1])



# Sol 1 : DFS
# cnt = 0
# def dfs(val,x,y):
#     global cnt
#     if val ==0:
#         if x==n-1 and y==n-1:
#             cnt+=1
#         return
    
#     # 오른쪽
#     if y+val <n:
#         dfs(grid[x][y+val], x, y+val)
#     if x+val <n:
#         dfs(grid[x+val][y], x+val, y)
# dfs(grid[0][0], 0,0)
# print(cnt)