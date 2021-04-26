import sys
input = sys.stdin.readline

n = int(input())
time = []
price = []
dp = [0]*(n+1)
for i in range(n):
    t, p = map(int,input().split())
    time.append(t)
    price.append(p)

max_earn = 0

for i in range(n):
    max_earn = max(max_earn, dp[i])
    if i+time[i] > n:
        continue
    dp[i + time[i]] = max(max_earn+price[i], dp[i+time[i]])

print(max(dp))
    