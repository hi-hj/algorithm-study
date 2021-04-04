import sys
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y,one,two):
    (x,y)
    (x,-one, y+one)
    (x-one-two, y+one-two)
    (x-two, y-two)

    return in_range(x,y) and in_range(x-one,y+one) \
        and in_range(x-one-two, y+one-two) and in_range(x-two,y-two)

def calc_area(x,y,one,two):
    calc_sum = 0
    # 1
    for i in range(one):
        calc_sum += grid[x-i][y+i]
    # 2
    for j in range(two):
        calc_sum += grid[x-one-j][y+one-j]
    # 3
    for i in range(one):
        calc_sum += grid[x-one-two+i][y+one-two-i]
    # 4
    for j in range(two):
        calc_sum += grid[x-two+j][y-two+j]
    return calc_sum

    

answer = 0
for i in range(1, n):
    for j in range(1, n-1):
        for one in range(1,n-1):
            for two in range(1,n-1):
                if can_go(i,j,one,two):
                    answer = max(answer, calc_area(i,j,one,two))

print(answer)

