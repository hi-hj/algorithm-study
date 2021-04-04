import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS
def find_block_max(cur_idx, find_sum):
    global answer
    if cur_idx == 3:
        answer = max(answer, find_sum)
        return

    for (x, y) in cur_list:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and (nx, ny) not in cur_list:
                cur_list.append((nx, ny))
                find_block_max(cur_idx+1, find_sum+grid[nx][ny])
                cur_list.pop()

answer = 0
cur_list = []
for i in range(n):
    for j in range(m):
        cur_list.append((i, j))
        find_block_max(0, grid[i][j])
        cur_list.pop()
print(answer)


