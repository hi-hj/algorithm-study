import pprint
import copy
import sys
def solution(rows, columns, queries):
    
    grid = [[0]*columns for _ in range(rows)]
    num = 1
    
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = num
            num+=1

    answer = []
    def rotate(x1, y1, x2, y2):

        numbers = []
        
        # ▶
        for i in range(y1, y2):
            numbers.append(grid[x1][i])
            # new_grid[x1][i+1] = grid[x1][i]
        # ▼
        for i in range(x1, x2):
            numbers.append(grid[i][y2])
            # new_grid[i+1][y2] = grid[i][y2]
            # min_num = min(min_num, grid[i][y2])
        # ◀
        for i in range(y2, y1, -1):
            numbers.append(grid[x2][i])
            # new_grid[x2][i-1] = grid[x2][i]
            # min_num = min(min_num, grid[x2][i])
        # ◀
        for i in range(x2, x1, -1):
            numbers.append(grid[i][y1])
            # new_grid[i-1][y1] = grid[i][y1]
            # min_num = min(min_num, grid[i][y1])
        last = numbers.pop()
        numbers.insert(0, last)
        index = 0

        for i in range(y1, y2):
            grid[x1][i] = numbers[index]
            index+=1

        # ▼
        for i in range(x1, x2):
            grid[i][y2] = numbers[index]
            index+=1

        # ◀
        for i in range(y2, y1, -1):
            grid[x2][i] = numbers[index]
            index+=1
        # ◀
        for i in range(x2, x1, -1):
            grid[i][y1] = numbers[index]
            index+=1
    
        return min(numbers)
    
    # RUN FUNCTION
    for x1, y1, x2, y2 in queries:
        # print(x1,y1,x2,y2)
        num = rotate(x1-1, y1-1, x2-1, y2-1)
        answer.append(num)
    
    # print(answer)
    return answer