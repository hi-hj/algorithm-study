import sys
import collections
input = sys.stdin.readline
n, k = map(int, input().split())

moving_walk = list(map(int, input().split()))
people=[False] * n
answer =0

walk = collections.deque()
for i in range(2*n):
    walk.append([False, moving_walk[i]])

up = []
down = []
for i in range(0,n):
    up.append((False, moving_walk[i]))
    down.append((False, moving_walk[i+n]))


def step_one():
    # Step 1
    up_to_down = up[n-1]
    down_to_up = down[n-1]
    for i in range(n-1, 0, -1):
        up[i] = up[i-1]
        down[i] = down[i-1]
    up[0] = down_to_up
    down[0] = up_to_down

def step_two():
    # step 2 : move people
    for i in range(n-1,-1,-1):
        if up[i][0] == True:
            if i+1==n or up[i+1][0]==True:
                continue
            else:
                people,stable = up[i]
                up[i] = (False, stable)
                people, stable = up[i+1]
                up[i+1] = (True, stable-1)

def step_thr():
    # step 3
    
    people, stable = up[0]
    if people == False and stable>0:
        up[0] = (True, stable-1)
    
    people, stable = up[n-1]
    if people == True:
        up[n-1] = (False, stable)

def step_fou():
    # step 4
    cnt=0
    for _, stable in up:
        if stable ==0:
            cnt +=1
    for _, stable in down:
        if stable ==0:
            cnt+=1

    if cnt >= k:
        return False
    return True

while step_fou():
    answer +=1
    step_one()
    step_two()
    step_thr()



print(answer)
