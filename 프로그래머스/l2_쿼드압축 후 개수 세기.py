from collections import deque

def check(x,y,n,arr):
    arr_sum = 0
    for i in range(x, x+n):
        arr_sum += sum(arr[i][y:y+n])
    return arr_sum

def solution(arr):
    answer = [0,0]
    
    n = len(arr)
    queue = deque()
    queue.append((0,0,n))
    
    while queue:
        x,y,n = queue.popleft()
        arr_sum = check(x,y,n,arr)
        
        if arr_sum == 0 and n>1:
            answer[0]+=1

        elif arr_sum == n*n and n>1:
            answer[1]+=1

        elif n>1:
            n = n//2
            queue.append((x,y,n))
            queue.append((x+n,y,n))
            queue.append((x,y+n, n))
            queue.append((x+n, y+n, n))
        elif n==1:
            if arr[x][y]==0: answer[0]+=1
            else: answer[1]+=1
    
    
    return answer


solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])