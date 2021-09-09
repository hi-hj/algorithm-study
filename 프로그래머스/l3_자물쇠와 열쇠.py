import pprint
import copy


def rotate90(arr):
    return list(zip(*arr[::-1]))


def solution(key, lock):
    n = len(lock)
    m = len(key)
    grid = [[0]*(m+2*n) for _ in range(m+2*n)]
    
    def check_lock_key(x,y,in_key):
        new_grid = copy.deepcopy(grid)
        # Grid에 key 넣기
        for i in range(m):
            for j in range(m):
                new_grid[i+x][j+y] += in_key[i][j]
        

        # 중간 Lock 체크
        for i in range(m, m+n):
            for j in range(m, m+n):
                if new_grid[i][j] == 0 or new_grid[i][j] ==2:
                    return False
        
        return True
    
    
    # Lock을 가운데에 고정
    for i in range(n):
        for j in range(n):
            grid[i+m][j+m] = lock[i][j]


    # 1. 실행
    for i in range(m+n):
        for j in range(m+n):
            for d in range(4):
                key = rotate90(key)
                if check_lock_key(i,j,key):
                    return True

    return False



solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], 
        [[1, 1, 1], [1, 1, 0], [1, 0, 1]])

