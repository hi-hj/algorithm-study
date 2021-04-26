import sys
import pprint
import copy
input = sys.stdin.readline

grid = [list(map(int, input().split())) for _ in range(10)]

visited = [[0]*10 for _ in range(10)]
cnt_paper = {1:0, 2:0, 3:0, 4:0, 5:0}
reverse_cnt_paper = {1:0, 2:0, 3:0, 4:0, 5:0}

def check_paper(n):
    
    for x in range(0, 11-n):
        for y in range(0, 11-n):
            if cnt_paper[n] ==5:
                break
            if grid[x][y]==1 and visited[x][y] ==0:
                check = True
                for nx in range(n):
                    for ny in range(n):
                        if grid[x+nx][y+ny] == 0 or visited[x+nx][y+ny]==1:
                            check = False
                            break
            else:
                check = False
            
            if grid[x][y]==1 and visited[x][y] ==0 and check == True:
                cnt_paper[n] +=1
                for nx in range(n):
                    for ny in range(n):
                        grid[x+nx][y+ny] = 0
                        visited[x+nx][y+ny] = 1
                
# def reverse_check_paper(n):
    
#     for x in range(9, n-2, -1):
#         for y in range(9, n-2,-1):

#             if reverse_cnt_paper[n] ==5:
#                 break
            
#             if reverse_grid[x][y]==1 and reverse_visited[x][y] ==0:
#                 check = True
#                 for nx in range(n):
#                     for ny in range(n):
#                         if reverse_grid[x-nx][y-ny] == 0 or reverse_visited[x-nx][y-ny]==1:
#                             check = False
#                             break
#             else:
#                 check = False
            
#             if reverse_grid[x][y]==1 and reverse_visited[x][y] ==0 and check == True:
#                 reverse_cnt_paper[n] +=1
#                 for nx in range(n):
#                     for ny in range(n):
#                         reverse_grid[x-nx][y-ny] = 0
#                         reverse_visited[x-nx][y-y] = 1

reverse_grid = copy.deepcopy(grid)
reverse_visited = copy.deepcopy(visited)

check_paper(5)
check_paper(4)
check_paper(3)
check_paper(2)
check_paper(1)


# reverse_check_paper(1)
# reverse_check_paper(2)
# reverse_check_paper(3)
# reverse_check_paper(4)
# reverse_check_paper(5)



calc_sum = 0

for i in range(10):
    calc_sum += sum(grid[i])
if calc_sum !=0:
    print(-1)
    exit()


answer = 0
for key, val in cnt_paper.items():
    answer += val
reverse_answer = 0
for key, val in reverse_cnt_paper.items():
    reverse_answer +=val

print(min(answer, reverse_answer))
