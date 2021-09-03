import pprint
from collections import deque


def solution(arr):
    N = len(arr)
    zero_cnt = 0
    one_cnt = 0

    def quad_check(x,y,n):
        cnt = 0
        for i in range(x, x+n):
            cnt += sum(arr[i][y:y+n])
        if cnt == 0:
            zero_cnt +=1
            return True
        elif cnt == n**2:
            one_cnt +=1
            return True
        return False

        

    
    pprint.pprint(arr)

    quad_check(0,0,4)


solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])