import copy
import sys
from itertools import permutations

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
calc_list = []
for _ in range(k):
    r, c, s = map(int, input().split())
    calc_list.append((r-1, c-1, s))


def move(r,c,s,in_grid):
    out_grid = copy.deepcopy(in_grid)

    while s>0:
        # 오른쪽
        for i in range(2*s):
            out_grid[r-s][c-s+1+i] = in_grid[r-s][c-s+i]
        # 아래쪽
        for i in range(2*s):
            out_grid[r-s+i+1][c+s] = in_grid[r-s+i][c+s]
        # 왼쪽
        for i in range(2*s):
            out_grid[r+s][c+s-i-1] = in_grid[r+s][c+s-i]
        # 위쪽
        for i in range(2*s):
            out_grid[r+s-i-1][c-s] = in_grid[r+s-i][c-s]
        s-=1
    
    return out_grid




# 1. 연산 순서 구하기
calc_list = list(permutations(calc_list,k))
min_a = sys.maxsize
for calc in calc_list:
    new_grid = copy.deepcopy(grid)
    # 2. 연산 하기
    for r,c,s in calc:
        new_grid = move(r,c,s,new_grid)
    # 3. A 값 구하기
    for i in range(n):
        min_a = min(min_a, sum(new_grid[i]))
print(min_a)