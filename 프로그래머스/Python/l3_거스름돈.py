
def solution(n, money):
    dp = [1] + [0]*n
    print(dp)
    for coin in money:
        print(coin)
        print(dp)
        for price in range(coin, n+1):
            if price >= coin:
                dp[price] += dp[price-coin]
        print(dp)
    return dp[n] % 1000000007

solution(4, [1,2,5])