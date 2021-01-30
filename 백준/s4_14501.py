import sys
input = sys.stdin.readline
import collections
sys.setrecursionlimit(1000)

n = int(input())
counter = collections.defaultdict(set)
for i in range(1, n+1):
    counter[i] = input().split()

results  = []
def dfs(day, profit):
    if day > n:
        results.append(profit)
        return
    # 실행 안함
    dfs(day+1, profit)
    # 실행 함
    if day + int(counter[day][0]) <= n+1:
        dfs(day+int(counter[day][0]), profit + int(counter[day][1]))

dfs(1, 0)


print(max(results))

    
