import sys
input = sys.stdin.readline
sys.setrecursionlimit(400)


r, c = map(int, input().split())

alpha = [list(input().rstrip()) for _ in range(r)]

max_cnt = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x, cnt, visited):

    global max_cnt
    if cnt == 26:
        max_cnt = 26
        return
    else:
        max_cnt = max(max_cnt, cnt)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<r and 0<=nx<c and alpha[ny][nx] not in visited:
            visited.append(alpha[ny][nx])
            dfs(ny, nx, cnt+1, visited)
            visited.pop()



dfs(0,0, 1, [alpha[0][0]])

print(max_cnt)



## 되는 코드 : 위에꺼는 시간 초과뜬다
### 하...
# import sys

# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def dfs(x, y, cnt):
#     global ans
#     if cnt == 26:
#         ans = 26
#         return
#     else:
#         ans = max(ans, cnt)
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < m and 0 <= ny < n:
#             num = to_num(nx, ny)
#             if c[num] == 0:
#                 c[num] = 1
#                 dfs(nx, ny, cnt+1)
#                 c[num] = 0

# def to_num(x, y):
#     return ord(a[x][y]) - ord('A')

# m, n = map(int, input().split())
# a = [list(map(str, input().strip())) for _ in range(m)]
# c, ans = [0]*26, 0

# c[to_num(0, 0)] = 1
# dfs(0, 0, 1)
# print(ans)
