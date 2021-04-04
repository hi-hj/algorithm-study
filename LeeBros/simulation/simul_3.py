import sys
input = sys.stdin.readline

n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]









def dfs(x, y, sum, one, two, go):
    
    if one==0 and two==0 and go==4:
        results.append(sum)
        return

    if go==0 or go==1:
        nx = x-1
        ny = y+1
        if 0<=nx and ny<n:
            dfs(nx, ny, sum+numbers[nx][ny], one+1, two, 1)
    
    elif go==1 or go==2:
        nx = x-1
        ny = y-1
        if 0<=nx and 0<=ny:
            dfs(nx, ny, sum+numbers[nx][ny], one, two+1, 2)
    
    elif go==2 or go==3 and one>0:
        nx = x+1
        ny = y-1
        if nx<n and 0<=ny:
            dfs(nx, ny, sum+numbers[nx][ny], one-1, two, 3)

    elif go==3 or go==4:
        nx = x+1
        ny = y+1
        if nx<n and ny<n:
            dfs(nx, ny, sum+numbers[nx][ny], one, two-1, 4) 


results = []
for i in range(1, n-1):
    for j in range(1, n-1):
        results = []
        dfs(n-i, j, numbers[n-i][j], 0, 0, 0)
        print(results)






# results = []
# for i in range(1, n-1):
#     for j in range(1, n-1):
#         visit = [[0]*n for _ in range(n)]
#         max_sum = 0
#         result = dfs(n-i, j, (0, 0), 0, numbers[n-i][j])
#         results.append(result)


# def dfs(x, y, (one, two), now, sum):
#     if now==4 and one==0 and two==0:
#         max_sum = max(max_sum, sum)
#         return max_sum


#     if now==0:
#         one_cnt = min(x, n-y)
#         for i in range(1, one_cnt):
#             if visit[x-i][y+i] ==0:
#                 visit[x-i][y+i] = 1
#                 dfs(x-i, y+i, (one+i, two), 1, sum+numbers[x-i][y+i])
    
#     if now==1:
#         two_cnt = min(x, y)
#         for i in range(1, two_cnt+1):
#             if visit[x-i][y-i] ==0:
#                 visit[x-i][y-i] = 1
#                 dfs(x-i, y+i, (one, two+i), 2, sum+numbers[x-i])

