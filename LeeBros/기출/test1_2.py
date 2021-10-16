import sys
from collections import deque

n = int(input())
block_prior = []
for _ in range(8):
    block_prior.append(list(map(int, input().split())))
blocks = []
for _ in range(n):
    k, c = map(int, input().split())
    blocks.append((k-1, c-1))

grid = [deque() for _ in range(4)]
print(grid)



for k, c in blocks:
    # c 가 -1인 경우는 잠시 보류
    # 1. BLOCK 떨구기
    grid[c].append(k)
print(grid)
grid[3].append(0)
min_len = min(map(len, grid))
print(min_len)
print(grid)
for ml in range(min_len):
    for i in range(4):
        grid[i].popleft()
print(grid)