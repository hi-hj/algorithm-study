import sys
import copy
input = sys.stdin.readline

n, m, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0

# def calc_max(cur_idx, cur_weight, cur_val):
#     global max_sum
#     if cur_idx == m:
#         if cur_weight <=

    
# def calc_max(one, two, cnt):
one_max = 0
two_max = 0

def find_one_max(cur_idx, cur_weight, cur_val, one_thieve):
    global one_max_cur
    if cur_idx == m:
        if cur_weight<=c:
            one_max_cur = max(one_max_cur, cur_val)
        return
    find_one_max(cur_idx+1, cur_weight, cur_val, one_thieve)
    find_one_max(cur_idx+1, cur_weight + one_thieve[cur_idx], cur_val + one_thieve[cur_idx]*one_thieve[cur_idx], one_thieve)

def find_two_max(cur_idx, cur_weight, cur_val, two_thieve):
    global two_max_cur
    if cur_idx == m:
        if cur_weight<=c:
            two_max_cur = max(two_max_cur, cur_val)
        return
    find_two_max(cur_idx+1, cur_weight, cur_val, two_thieve)
    find_two_max(cur_idx+1, cur_weight + two_thieve[cur_idx], cur_val + two_thieve[cur_idx]*two_thieve[cur_idx], two_thieve)


def find_max(one_thieve, two_thieve):
    global max_sum
    global one_max_cur
    global two_max_cur
    one_max_cur = 0
    two_max_cur = 0
    find_one_max(0, 0, 0, one_thieve)
    find_two_max(0, 0, 0, two_thieve)
    # print(max_sum, one_max, two_max)
    max_sum = max(max_sum, one_max_cur + two_max_cur)
    


    
def START_STEAL(x, y, m):
    global max_sum
    one_thieve = []
    for i in range(m):
        one_thieve.append(grid[x][y+i])
    
    # 같은 열
    for i in range(y+m, n-m+1):
        two_thieve = []
        for j in range(m):
            two_thieve.append(grid[x][i+j])
        # print(one_thieve, two_thieve)
        find_max(one_thieve, two_thieve)
    # 다른 열
    for i in range(x+1, n):
        for j in range(n):
            if j + m<=n:
                two_thieve = []
                for k in range(m):
                    two_thieve.append(grid[i][j+k])
                # print(one_thieve, two_thieve)
                find_max(one_thieve, two_thieve)
    
    
    


for i in range(n):
    for j in range(n):
        if j + m <= n:
            START_STEAL(i, j, m)
print(max_sum)