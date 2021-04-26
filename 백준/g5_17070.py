from collections import deque
import sys
input = sys.stdin.readline
def dfs(x, y, direction):
    global count
    if x == n - 1 and y == n - 1: count += 1
    if direction == 0:
        if y + 1 < n and s[x][y + 1] == 0: dfs(x, y + 1, 0)
        if x + 1 < n and y + 1 < n:
            if s[x][y + 1] == 0 and s[x + 1][y + 1] == 0 and s[x + 1][y] == 0:
                dfs(x + 1, y + 1, 2)
    elif direction == 1:
        if x + 1 < n and s[x + 1][y] == 0: dfs(x + 1, y, 1)
        if x + 1 < n and y + 1 < n:
            if s[x][y + 1] == 0 and s[x + 1][y + 1] == 0 and s[x + 1][y] == 0:
                dfs(x + 1, y + 1, 2)
    elif direction == 2:
        if y + 1 < n and s[x][y + 1] == 0: dfs(x, y + 1, 0)
        if x + 1 < n and s[x + 1][y] == 0: dfs(x + 1, y, 1)
        if x + 1 < n and y + 1 < n:
            if s[x][y + 1] == 0 and s[x + 1][y + 1] == 0 and s[x + 1][y] == 0:
                dfs(x + 1, y + 1, 2)
n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
count = 0
dfs(0, 1, 0)
print(count)