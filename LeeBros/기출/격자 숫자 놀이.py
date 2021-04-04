import sys
import collections
import copy

input = sys.stdin.readline

r,c,k = map(int, input().split())
r,c = r-1,c-1

grid = [list(map(int, input().split())) for _ in range(3)]


def make_new_grid(num_list):
    check_dict = {}
    for num in num_list:
        if num in check_dict and num!=0:
            check_dict[num] +=1
        elif num!=0:
            check_dict[num] =1
    check_dict = sorted(check_dict.items(), key = lambda item:(item[1], item[0]))
    new_num = []
    for val, num in check_dict:
        new_num.append(val)
        new_num.append(num)
    return new_num



answer = 0





while True:
    
    # 행 / 열
    n,m = len(grid) ,len(grid[0])

    # 100 넘어가는 경우 절삭
    if n >100:
        n = 100
        new_grid = [[0]*m for _ in range(100)]
        for i in range(100):
            for j in range(m):
                new_grid[i][j] = grid[i][j]
        grid = copy.deepcopy(new_grid)
    if m>100:
        m = 100
        new_grid = [[0]*100 for _ in range(n)]
        for i in range(n):
            for j in range(100):
                new_grid[i][j] = grid[i][j]
        grid = copy.deepcopy(new_grid)
    
    if r<n and c <m:
        if grid[r][c] ==k:
            print(answer)
            exit()
    if n>=m:
        # 1. 행 >= 열
        for i in range(n):
            grid[i] = make_new_grid(grid[i])

        max_m = 0
        for i in range(n):
            max_m = max(max_m, len(grid[i]))

        new_grid = [[0]*max_m for _ in range(n)]
        for i in range(n):
            for j, num in enumerate(grid[i]):
                new_grid[i][j] = num

        grid = copy.deepcopy(new_grid)
        answer +=1


    # 2. 열 > 행
    else:

        
        new_grid = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new_grid[j][i] = grid[i][j]

        for i in range(m):
            new_grid[i] = make_new_grid(new_grid[i])
        max_m = 0
        for i in range(m):
            max_m = max(max_m, len(new_grid[i]))
        grid = [[0]*max_m for _ in range(m)]
        for i in range(m):
            for j, num in enumerate(new_grid[i]):
                grid[i][j] = num

        new_grid = [[0]*m for _ in range(max_m)]
        for i in range(m):
            for j in range(max_m):
                new_grid[j][i] = grid[i][j]


        grid = copy.deepcopy(new_grid)
        answer +=1
    
    n,m = len(grid) ,len(grid[0])
    if answer >=100:
        break

    if r<n and c <m:
        if grid[r][c] ==k:
            print(answer)
            exit()


print(-1)


    

