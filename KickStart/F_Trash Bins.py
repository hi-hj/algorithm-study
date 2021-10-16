import sys

T = int(input())

for t in range(1,T+1):
    N = int(input())
    houses = list(input())

    left = [0]*N
    last_left = sys.maxsize

    right = [0]*N
    last_right = -sys.maxsize

    answer = [0]*N

    for i in range(N):
        if houses[i]=='1':
            last_left = i
        elif houses[i]=='0':
            if last_left == sys.maxsize:
                left[i]=sys.maxsize
            else:left[i] = i - last_left
    
    for i in range(N-1, -1, -1):
        if houses[i]=='1':
            last_right = i
        elif houses[i]=='0':
            if last_right == -sys.maxsize: right[i]=sys.maxsize
            else: right[i] = last_right - i
    
    # print(left, right)
    for i in range(N):
        answer[i] = min(left[i],right[i])
    print("Case #" +str(t)+": "+str(sum(answer)))