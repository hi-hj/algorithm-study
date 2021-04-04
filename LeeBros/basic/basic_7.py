import sys
input = sys.stdin.readline
import collections

n = int(input())

group = list(map(int, input().split()))


group = sorted(group)

results = []

for i in range(n):
    min_num = group.pop(0)
    max_num = group.pop()
    results.append(min_num+max_num)

print(max(results))