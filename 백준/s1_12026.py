import sys
n = int(input())
block = input()

dp = [0]*n
num_alpha = {0:'B', 1:'O', 2:'J'}
alpha_num = {'B':0, 'O':1, 'J':2}

now_alpha = 0 # 'B'


for i in range(1, n):
    now_alpha = block[i]
    before_alpha_index = (alpha_num[now_alpha]-1)%3
    before_alpha = num_alpha[before_alpha_index]
    cnt = sys.maxsize
    
    for j in range(i-1, -1,-1):
        if block[j] == before_alpha:
            cnt = min(cnt, dp[j] + (i-j)**2)
    dp[i] = cnt

if dp[-1] ==sys.maxsize:
    print(-1)
else:
    print(dp[-1])

